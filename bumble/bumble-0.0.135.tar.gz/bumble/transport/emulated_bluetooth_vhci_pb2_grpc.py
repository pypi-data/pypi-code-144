# Copyright 2021-2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import emulated_bluetooth_packets_pb2 as emulated__bluetooth__packets__pb2


class VhciForwardingServiceStub(object):
    """This is a service which allows you to directly intercept the VHCI packets
    that are coming and going to the device before they are delivered to
    the rootcanal service described below.

    This service is usually not available on the emulator, and must be explictly
    requested from the commandline.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.attachVhci = channel.stream_stream(
            '/android.emulation.bluetooth.VhciForwardingService/attachVhci',
            request_serializer=emulated__bluetooth__packets__pb2.HCIPacket.SerializeToString,
            response_deserializer=emulated__bluetooth__packets__pb2.HCIPacket.FromString,
        )


class VhciForwardingServiceServicer(object):
    """This is a service which allows you to directly intercept the VHCI packets
    that are coming and going to the device before they are delivered to
    the rootcanal service described below.

    This service is usually not available on the emulator, and must be explictly
    requested from the commandline.
    """

    def attachVhci(self, request_iterator, context):
        """This attach directly to /dev/vhci inside the android guest if available

        - This will disable root canal.
        - You will have to provide your own virtual bluetooth chip.

        Some things to be aware of:
        - Only one client can be active.
        - Registering when bluetooth is active in android can result in
        undefined behavior.
        - If a client disconnects, rootcanal will be activated again

        Status codes:
        -  FAILED_PRECONDITION (code 9) If another client is controlling /dev/vhci.

        This is an internal testing only interface, and is NOT publicly
        supported.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_VhciForwardingServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'attachVhci': grpc.stream_stream_rpc_method_handler(
            servicer.attachVhci,
            request_deserializer=emulated__bluetooth__packets__pb2.HCIPacket.FromString,
            response_serializer=emulated__bluetooth__packets__pb2.HCIPacket.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'android.emulation.bluetooth.VhciForwardingService', rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class VhciForwardingService(object):
    """This is a service which allows you to directly intercept the VHCI packets
    that are coming and going to the device before they are delivered to
    the rootcanal service described below.

    This service is usually not available on the emulator, and must be explictly
    requested from the commandline.
    """

    @staticmethod
    def attachVhci(
        request_iterator,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.stream_stream(
            request_iterator,
            target,
            '/android.emulation.bluetooth.VhciForwardingService/attachVhci',
            emulated__bluetooth__packets__pb2.HCIPacket.SerializeToString,
            emulated__bluetooth__packets__pb2.HCIPacket.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
