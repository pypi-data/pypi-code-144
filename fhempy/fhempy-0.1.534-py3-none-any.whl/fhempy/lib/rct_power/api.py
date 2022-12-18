"""
Based on
https://github.com/weltenwort/home-assistant-rct-power-integration/blob/main/custom_components/rct_power/lib/api.py
"""
from asyncio import StreamReader, StreamWriter, TimeoutError, open_connection
from asyncio.locks import Lock
from dataclasses import dataclass
from datetime import datetime
import struct
from typing import Dict, List, Optional, Tuple, TypeVar, Union

import async_timeout
from rctclient.exceptions import FrameCRCMismatch, FrameLengthExceeded, InvalidCommand
from rctclient.frame import ReceiveFrame, SendFrame
from rctclient.registry import REGISTRY
from rctclient.types import Command, EventEntry
from rctclient.utils import decode_value, encode_value

CONNECTION_TIMEOUT = 20
READ_TIMEOUT = 2
INVERTER_SN_OID = 0x7924ABD9

ApiResponseValue = Union[
    bool,
    bytes,
    float,
    int,
    str,
    Tuple[datetime, Dict[datetime, int]],
    Tuple[datetime, Dict[datetime, EventEntry]],
]
DefaultResponseValue = TypeVar("DefaultResponseValue")


@dataclass
class BaseApiResponse:
    object_id: int
    object_name: str
    time: datetime


@dataclass
class ValidApiResponse(BaseApiResponse):
    value: ApiResponseValue


@dataclass
class InvalidApiResponse(BaseApiResponse):
    cause: str


ApiResponse = Union[ValidApiResponse, InvalidApiResponse]
RctPowerData = Dict[int, ApiResponse]


def get_valid_response_value_or(
    response: Optional[ApiResponse],
    defaultValue: DefaultResponseValue,
) -> Union[ApiResponseValue, DefaultResponseValue]:
    if isinstance(response, ValidApiResponse):
        return response.value
    else:
        return defaultValue


class RctPowerApiClient:
    def __init__(self, logger, hostname: str, port: int) -> None:
        """Sample API Client."""
        self.logger = logger
        self._hostname = hostname
        self._port = port

        # ensure only one connection at a time is established because the
        # inverter's firmware doesn't handle it well at the time of writing
        self._connection_lock = Lock()

    async def get_serial_number(self) -> Optional[str]:
        inverter_data = await self.async_get_data([INVERTER_SN_OID])

        inverter_sn_response = inverter_data.get(INVERTER_SN_OID)

        if isinstance(inverter_sn_response, ValidApiResponse) and isinstance(
            inverter_sn_response.value, str
        ):
            return inverter_sn_response.value
        else:
            return None

    async def async_send_data(self, object_id: int, value) -> RctPowerData:
        async with self._connection_lock:
            async with async_timeout.timeout(CONNECTION_TIMEOUT):
                reader, writer = await open_connection(
                    host=self._hostname, port=self._port
                )

                try:
                    if reader.at_eof():
                        raise Exception("Read stream closed")

                    await self._write_object(
                        reader=reader, writer=writer, object_id=object_id, value=value
                    )
                finally:
                    writer.close()

    async def _write_object(
        self, reader: StreamReader, writer: StreamWriter, object_id: int, value
    ):
        oinfo = REGISTRY.get_by_id(object_id)
        object_name = oinfo.name
        payload = encode_value(oinfo.request_data_type, value)
        send_command_frame = SendFrame(
            command=Command.WRITE, id=object_id, payload=payload
        )

        self.logger.debug(
            "Writing RCT Power data (%s) for object %x (%s)...",
            str(value),
            object_id,
            object_name,
        )
        request_time = datetime.now()

        try:
            async with async_timeout.timeout(READ_TIMEOUT):
                await writer.drain()
                writer.write(send_command_frame.data)

                # loop until we return or time out
                while True:
                    response_frame = ReceiveFrame()

                    while not response_frame.complete() and not reader.at_eof():
                        raw_response = await reader.read(1)

                        if len(raw_response) > 0:
                            response_frame.consume(raw_response)

                    if response_frame.complete():
                        response_object_info = REGISTRY.get_by_id(response_frame.id)
                        data_type = response_object_info.response_data_type
                        received_object_name = response_object_info.name

                        # ignore, if this is not the answer to the latest request
                        if object_id != response_frame.id:
                            self.logger.debug(
                                "Mismatch of requested and received object ids: requested %x (%s), but received %x (%s)",
                                object_id,
                                object_name,
                                response_frame.id,
                                received_object_name,
                            )
                            continue

                        decoded_value: Union[
                            bool,
                            bytes,
                            float,
                            int,
                            str,
                            Tuple[datetime, Dict[datetime, int]],
                            Tuple[datetime, Dict[datetime, EventEntry]],
                        ] = decode_value(
                            data_type, response_frame.data
                        )  # type: ignore

                        self.logger.debug(
                            "Decoded data for object %x (%s): %s",
                            response_frame.id,
                            received_object_name,
                            decoded_value,
                        )

                        return ValidApiResponse(
                            object_id=object_id,
                            object_name=object_name,
                            time=request_time,
                            value=decoded_value,
                        )
                    else:
                        self.logger.debug(
                            "Error decoding object %x (%s): %s",
                            object_id,
                            object_name,
                            response_frame.data,
                        )
                        return InvalidApiResponse(
                            object_id=object_id,
                            object_name=object_name,
                            time=request_time,
                            cause="INCOMPLETE",
                        )

        except TimeoutError as exc:
            self.logger.debug(
                "Error reading object %x (%s): %s", object_id, object_name, str(exc)
            )
            return InvalidApiResponse(
                object_id=object_id,
                object_name=object_name,
                time=request_time,
                cause="OBJECT_READ_TIMEOUT",
            )
        except FrameCRCMismatch as exc:
            self.logger.debug(
                "Error reading object %x (%s): %s", object_id, object_name, str(exc)
            )
            return InvalidApiResponse(
                object_id=object_id,
                object_name=object_name,
                time=request_time,
                cause="CRC_ERROR",
            )
        except FrameLengthExceeded as exc:
            self.logger.debug(
                "Error reading object %x (%s): %s", object_id, object_name, str(exc)
            )
            return InvalidApiResponse(
                object_id=object_id,
                object_name=object_name,
                time=request_time,
                cause="FRAME_LENGTH_EXCEEDED",
            )
        except InvalidCommand as exc:
            self.logger.debug(
                "Error reading object %x (%s): %s", object_id, object_name, str(exc)
            )
            return InvalidApiResponse(
                object_id=object_id,
                object_name=object_name,
                time=request_time,
                cause="INVALID_COMMAND",
            )
        except struct.error as exc:
            self.logger.debug(
                "Error reading object %x (%s): %s", object_id, object_name, str(exc)
            )
            return InvalidApiResponse(
                object_id=object_id,
                object_name=object_name,
                time=request_time,
                cause="PARSING_ERROR",
            )
        except Exception as exc:
            self.logger.debug(
                "Error reading object %x (%s): %s", object_id, object_name, str(exc)
            )
            return InvalidApiResponse(
                object_id=object_id,
                object_name=object_name,
                time=request_time,
                cause="UNKNOWN_ERROR",
            )

    async def async_get_data(self, object_ids: List[int]) -> RctPowerData:
        async with self._connection_lock:
            async with async_timeout.timeout(CONNECTION_TIMEOUT):
                reader, writer = await open_connection(
                    host=self._hostname, port=self._port
                )

                try:
                    if reader.at_eof():
                        raise Exception("Read stream closed")

                    return {
                        object_id: await self._read_object(
                            reader=reader, writer=writer, object_id=object_id
                        )
                        for object_id in object_ids
                    }
                finally:
                    writer.close()

    async def _read_object(
        self, reader: StreamReader, writer: StreamWriter, object_id: int
    ):
        object_name = REGISTRY.get_by_id(object_id).name
        read_command_frame = SendFrame(command=Command.READ, id=object_id)

        self.logger.debug(
            "Requesting RCT Power data for object %x (%s)...", object_id, object_name
        )
        request_time = datetime.now()

        try:
            async with async_timeout.timeout(READ_TIMEOUT):
                await writer.drain()
                writer.write(read_command_frame.data)

                # loop until we return or time out
                while True:
                    response_frame = ReceiveFrame()

                    while not response_frame.complete() and not reader.at_eof():
                        raw_response = await reader.read(1)

                        if len(raw_response) > 0:
                            response_frame.consume(raw_response)

                    if response_frame.complete():
                        response_object_info = REGISTRY.get_by_id(response_frame.id)
                        data_type = response_object_info.response_data_type
                        received_object_name = response_object_info.name

                        # ignore, if this is not the answer to the latest request
                        if object_id != response_frame.id:
                            self.logger.debug(
                                "Mismatch of requested and received object ids: requested %x (%s), but received %x (%s)",
                                object_id,
                                object_name,
                                response_frame.id,
                                received_object_name,
                            )
                            continue

                        decoded_value: Union[
                            bool,
                            bytes,
                            float,
                            int,
                            str,
                            Tuple[datetime, Dict[datetime, int]],
                            Tuple[datetime, Dict[datetime, EventEntry]],
                        ] = decode_value(
                            data_type, response_frame.data
                        )  # type: ignore

                        self.logger.debug(
                            "Decoded data for object %x (%s): %s",
                            response_frame.id,
                            received_object_name,
                            decoded_value,
                        )

                        return ValidApiResponse(
                            object_id=object_id,
                            object_name=object_name,
                            time=request_time,
                            value=decoded_value,
                        )
                    else:
                        self.logger.debug(
                            "Error decoding object %x (%s): %s",
                            object_id,
                            object_name,
                            response_frame.data,
                        )
                        return InvalidApiResponse(
                            object_id=object_id,
                            object_name=object_name,
                            time=request_time,
                            cause="INCOMPLETE",
                        )

        except TimeoutError as exc:
            self.logger.debug(
                "Error reading object %x (%s): %s", object_id, object_name, str(exc)
            )
            return InvalidApiResponse(
                object_id=object_id,
                object_name=object_name,
                time=request_time,
                cause="OBJECT_READ_TIMEOUT",
            )
        except FrameCRCMismatch as exc:
            self.logger.debug(
                "Error reading object %x (%s): %s", object_id, object_name, str(exc)
            )
            return InvalidApiResponse(
                object_id=object_id,
                object_name=object_name,
                time=request_time,
                cause="CRC_ERROR",
            )
        except FrameLengthExceeded as exc:
            self.logger.debug(
                "Error reading object %x (%s): %s", object_id, object_name, str(exc)
            )
            return InvalidApiResponse(
                object_id=object_id,
                object_name=object_name,
                time=request_time,
                cause="FRAME_LENGTH_EXCEEDED",
            )
        except InvalidCommand as exc:
            self.logger.debug(
                "Error reading object %x (%s): %s", object_id, object_name, str(exc)
            )
            return InvalidApiResponse(
                object_id=object_id,
                object_name=object_name,
                time=request_time,
                cause="INVALID_COMMAND",
            )
        except struct.error as exc:
            self.logger.debug(
                "Error reading object %x (%s): %s", object_id, object_name, str(exc)
            )
            return InvalidApiResponse(
                object_id=object_id,
                object_name=object_name,
                time=request_time,
                cause="PARSING_ERROR",
            )
        except Exception as exc:
            self.logger.debug(
                "Error reading object %x (%s): %s", object_id, object_name, str(exc)
            )
            return InvalidApiResponse(
                object_id=object_id,
                object_name=object_name,
                time=request_time,
                cause="UNKNOWN_ERROR",
            )
