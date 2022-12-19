#
# Copyright (c) 2022 Airbyte, Inc., all rights reserved.
#

# generated by datamodel-codegen:
#   filename:  airbyte_protocol.yaml

from __future__ import annotations

from enum import Enum
from typing import Any, Dict, List, Optional, Union

from pydantic import AnyUrl, BaseModel, Extra, Field


class Type(Enum):
    RECORD = "RECORD"
    STATE = "STATE"
    LOG = "LOG"
    SPEC = "SPEC"
    CONNECTION_STATUS = "CONNECTION_STATUS"
    CATALOG = "CATALOG"
    TRACE = "TRACE"
    CONTROL = "CONTROL"


class AirbyteRecordMessage(BaseModel):
    class Config:
        extra = Extra.allow

    namespace: Optional[str] = Field(None, description="namespace the data is associated with")
    stream: str = Field(..., description="stream the data is associated with")
    data: Dict[str, Any] = Field(..., description="record data")
    emitted_at: int = Field(
        ...,
        description="when the data was emitted from the source. epoch in millisecond.",
    )


class AirbyteStateType(Enum):
    GLOBAL = "GLOBAL"
    STREAM = "STREAM"
    LEGACY = "LEGACY"


class StreamDescriptor(BaseModel):
    class Config:
        extra = Extra.allow

    name: str
    namespace: Optional[str] = None


class AirbyteStateBlob(BaseModel):
    pass

    class Config:
        extra = Extra.allow


class Level(Enum):
    FATAL = "FATAL"
    ERROR = "ERROR"
    WARN = "WARN"
    INFO = "INFO"
    DEBUG = "DEBUG"
    TRACE = "TRACE"


class AirbyteLogMessage(BaseModel):
    class Config:
        extra = Extra.allow

    level: Level = Field(..., description="log level")
    message: str = Field(..., description="log message")
    stack_trace: Optional[str] = Field(
        None,
        description="an optional stack trace if the log message corresponds to an exception",
    )


class TraceType(Enum):
    ERROR = "ERROR"
    ESTIMATE = "ESTIMATE"


class FailureType(Enum):
    system_error = "system_error"
    config_error = "config_error"


class AirbyteErrorTraceMessage(BaseModel):
    class Config:
        extra = Extra.allow

    message: str = Field(..., description="A user-friendly message that indicates the cause of the error")
    internal_message: Optional[str] = Field(None, description="The internal error that caused the failure")
    stack_trace: Optional[str] = Field(None, description="The full stack trace of the error")
    failure_type: Optional[FailureType] = Field(None, description="The type of error")


class EstimateType(Enum):
    STREAM = "STREAM"
    SYNC = "SYNC"


class AirbyteEstimateTraceMessage(BaseModel):
    class Config:
        extra = Extra.allow

    name: str = Field(..., description="The name of the stream")
    type: EstimateType = Field(
        ...,
        description="Estimates are either per-stream (STREAM) or for the entire sync (SYNC). STREAM is preferred, and requires the source to count how many records are about to be emitted per-stream (e.g. there will be 100 rows from this table emitted). For the rare source which cannot tell which stream a record belongs to before reading (e.g. CDC databases), SYNC estimates can be emitted. Sources should not emit both STREAM and SOURCE estimates within a sync.\n",
        title="estimate type",
    )
    namespace: Optional[str] = Field(None, description="The namespace of the stream")
    row_estimate: Optional[int] = Field(
        None,
        description="The estimated number of rows to be emitted by this sync for this stream",
    )
    byte_estimate: Optional[int] = Field(
        None,
        description="The estimated number of bytes to be emitted by this sync for this stream",
    )


class OrchestratorType(Enum):
    CONNECTOR_CONFIG = "CONNECTOR_CONFIG"


class AirbyteControlConnectorConfigMessage(BaseModel):
    class Config:
        extra = Extra.allow

    config: Dict[str, Any] = Field(..., description="the config items from this connector's spec to update")


class Status(Enum):
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"


class AirbyteConnectionStatus(BaseModel):
    class Config:
        extra = Extra.allow

    status: Status
    message: Optional[str] = None


class SyncMode(Enum):
    full_refresh = "full_refresh"
    incremental = "incremental"


class DestinationSyncMode(Enum):
    append = "append"
    overwrite = "overwrite"
    append_dedup = "append_dedup"


class OAuth2Specification(BaseModel):
    class Config:
        extra = Extra.allow

    rootObject: Optional[List[Union[str, int]]] = Field(
        None,
        description="A list of strings representing a pointer to the root object which contains any oauth parameters in the ConnectorSpecification.\nExamples:\nif oauth parameters were contained inside the top level, rootObject=[] If they were nested inside another object {'credentials': {'app_id' etc...}, rootObject=['credentials'] If they were inside a oneOf {'switch': {oneOf: [{client_id...}, {non_oauth_param]}},  rootObject=['switch', 0] ",
    )
    oauthFlowInitParameters: Optional[List[List[str]]] = Field(
        None,
        description="Pointers to the fields in the rootObject needed to obtain the initial refresh/access tokens for the OAuth flow. Each inner array represents the path in the rootObject of the referenced field. For example. Assume the rootObject contains params 'app_secret', 'app_id' which are needed to get the initial refresh token. If they are not nested in the rootObject, then the array would look like this [['app_secret'], ['app_id']] If they are nested inside an object called 'auth_params' then this array would be [['auth_params', 'app_secret'], ['auth_params', 'app_id']]",
    )
    oauthFlowOutputParameters: Optional[List[List[str]]] = Field(
        None,
        description="Pointers to the fields in the rootObject which can be populated from successfully completing the oauth flow using the init parameters. This is typically a refresh/access token. Each inner array represents the path in the rootObject of the referenced field.",
    )


class AuthType(Enum):
    oauth2_0 = "oauth2.0"


class AuthSpecification(BaseModel):
    auth_type: Optional[AuthType] = None
    oauth2Specification: Optional[OAuth2Specification] = Field(
        None,
        description="If the connector supports OAuth, this field should be non-null.",
    )


class AuthFlowType(Enum):
    oauth2_0 = "oauth2.0"
    oauth1_0 = "oauth1.0"


class OAuthConfigSpecification(BaseModel):
    class Config:
        extra = Extra.allow

    oauth_user_input_from_connector_config_specification: Optional[Dict[str, Any]] = Field(
        None,
        description="OAuth specific blob. This is a Json Schema used to validate Json configurations used as input to OAuth.\nMust be a valid non-nested JSON that refers to properties from ConnectorSpecification.connectionSpecification\nusing special annotation 'path_in_connector_config'.\nThese are input values the user is entering through the UI to authenticate to the connector, that might also shared\nas inputs for syncing data via the connector.\n\nExamples:\n\nif no connector values is shared during oauth flow, oauth_user_input_from_connector_config_specification=[]\nif connector values such as 'app_id' inside the top level are used to generate the API url for the oauth flow,\n  oauth_user_input_from_connector_config_specification={\n    app_id: {\n      type: string\n      path_in_connector_config: ['app_id']\n    }\n  }\nif connector values such as 'info.app_id' nested inside another object are used to generate the API url for the oauth flow,\n  oauth_user_input_from_connector_config_specification={\n    app_id: {\n      type: string\n      path_in_connector_config: ['info', 'app_id']\n    }\n  }",
    )
    complete_oauth_output_specification: Optional[Dict[str, Any]] = Field(
        None,
        description="OAuth specific blob. This is a Json Schema used to validate Json configurations produced by the OAuth flows as they are\nreturned by the distant OAuth APIs.\nMust be a valid JSON describing the fields to merge back to `ConnectorSpecification.connectionSpecification`.\nFor each field, a special annotation `path_in_connector_config` can be specified to determine where to merge it,\n\nExamples:\n\n    complete_oauth_output_specification={\n      refresh_token: {\n        type: string,\n        path_in_connector_config: ['credentials', 'refresh_token']\n      }\n    }",
    )
    complete_oauth_server_input_specification: Optional[Dict[str, Any]] = Field(
        None,
        description="OAuth specific blob. This is a Json Schema used to validate Json configurations persisted as Airbyte Server configurations.\nMust be a valid non-nested JSON describing additional fields configured by the Airbyte Instance or Workspace Admins to be used by the\nserver when completing an OAuth flow (typically exchanging an auth code for refresh token).\n\nExamples:\n\n    complete_oauth_server_input_specification={\n      client_id: {\n        type: string\n      },\n      client_secret: {\n        type: string\n      }\n    }",
    )
    complete_oauth_server_output_specification: Optional[Dict[str, Any]] = Field(
        None,
        description="OAuth specific blob. This is a Json Schema used to validate Json configurations persisted as Airbyte Server configurations that\nalso need to be merged back into the connector configuration at runtime.\nThis is a subset configuration of `complete_oauth_server_input_specification` that filters fields out to retain only the ones that\nare necessary for the connector to function with OAuth. (some fields could be used during oauth flows but not needed afterwards, therefore\nthey would be listed in the `complete_oauth_server_input_specification` but not `complete_oauth_server_output_specification`)\nMust be a valid non-nested JSON describing additional fields configured by the Airbyte Instance or Workspace Admins to be used by the\nconnector when using OAuth flow APIs.\nThese fields are to be merged back to `ConnectorSpecification.connectionSpecification`.\nFor each field, a special annotation `path_in_connector_config` can be specified to determine where to merge it,\n\nExamples:\n\n      complete_oauth_server_output_specification={\n        client_id: {\n          type: string,\n          path_in_connector_config: ['credentials', 'client_id']\n        },\n        client_secret: {\n          type: string,\n          path_in_connector_config: ['credentials', 'client_secret']\n        }\n      }",
    )


class AirbyteStreamState(BaseModel):
    class Config:
        extra = Extra.allow

    stream_descriptor: StreamDescriptor
    stream_state: Optional[AirbyteStateBlob] = None


class AirbyteGlobalState(BaseModel):
    class Config:
        extra = Extra.allow

    shared_state: Optional[AirbyteStateBlob] = None
    stream_states: List[AirbyteStreamState]


class AirbyteTraceMessage(BaseModel):
    class Config:
        extra = Extra.allow

    type: TraceType = Field(..., description="the type of trace message", title="trace type")
    emitted_at: float = Field(..., description="the time in ms that the message was emitted")
    error: Optional[AirbyteErrorTraceMessage] = Field(None, description="error trace message: the error object")
    estimate: Optional[AirbyteEstimateTraceMessage] = Field(
        None,
        description="Estimate trace message: a guess at how much data will be produced in this sync",
    )


class AirbyteControlMessage(BaseModel):
    class Config:
        extra = Extra.allow

    type: OrchestratorType = Field(..., description="the type of orchestrator message", title="orchestrator type")
    emitted_at: float = Field(..., description="the time in ms that the message was emitted")
    connectorConfig: Optional[AirbyteControlConnectorConfigMessage] = Field(
        None,
        description="connector config orchestrator message: the updated config for the platform to store for this connector",
    )


class AirbyteStream(BaseModel):
    class Config:
        extra = Extra.allow

    name: str = Field(..., description="Stream's name.")
    json_schema: Dict[str, Any] = Field(..., description="Stream schema using Json Schema specs.")
    supported_sync_modes: List[SyncMode] = Field(..., description="List of sync modes supported by this stream.", min_items=1)
    source_defined_cursor: Optional[bool] = Field(
        None,
        description="If the source defines the cursor field, then any other cursor field inputs will be ignored. If it does not, either the user_provided one is used, or the default one is used as a backup.",
    )
    default_cursor_field: Optional[List[str]] = Field(
        None,
        description="Path to the field that will be used to determine if a record is new or modified since the last sync. If not provided by the source, the end user will have to specify the comparable themselves.",
    )
    source_defined_primary_key: Optional[List[List[str]]] = Field(
        None,
        description="If the source defines the primary key, paths to the fields that will be used as a primary key. If not provided by the source, the end user will have to specify the primary key themselves.",
    )
    namespace: Optional[str] = Field(
        None,
        description="Optional Source-defined namespace. Currently only used by JDBC destinations to determine what schema to write to. Airbyte streams from the same sources should have the same namespace.",
    )


class ConfiguredAirbyteStream(BaseModel):
    class Config:
        extra = Extra.allow

    stream: AirbyteStream
    sync_mode: SyncMode
    cursor_field: Optional[List[str]] = Field(
        None,
        description="Path to the field that will be used to determine if a record is new or modified since the last sync. This field is REQUIRED if `sync_mode` is `incremental`. Otherwise it is ignored.",
    )
    destination_sync_mode: DestinationSyncMode
    primary_key: Optional[List[List[str]]] = Field(
        None,
        description="Paths to the fields that will be used as primary key. This field is REQUIRED if `destination_sync_mode` is `*_dedup`. Otherwise it is ignored.",
    )


class AdvancedAuth(BaseModel):
    auth_flow_type: Optional[AuthFlowType] = None
    predicate_key: Optional[List[str]] = Field(
        None,
        description="Json Path to a field in the connectorSpecification that should exist for the advanced auth to be applicable.",
    )
    predicate_value: Optional[str] = Field(
        None,
        description="Value of the predicate_key fields for the advanced auth to be applicable.",
    )
    oauth_config_specification: Optional[OAuthConfigSpecification] = None


class ConnectorSpecification(BaseModel):
    class Config:
        extra = Extra.allow

    documentationUrl: Optional[AnyUrl] = None
    changelogUrl: Optional[AnyUrl] = None
    connectionSpecification: Dict[str, Any] = Field(
        ...,
        description="ConnectorDefinition specific blob. Must be a valid JSON string.",
    )
    supportsIncremental: Optional[bool] = Field(
        None,
        description="(deprecated) If the connector supports incremental mode or not.",
    )
    supportsNormalization: Optional[bool] = Field(False, description="If the connector supports normalization or not.")
    supportsDBT: Optional[bool] = Field(False, description="If the connector supports DBT or not.")
    supported_destination_sync_modes: Optional[List[DestinationSyncMode]] = Field(
        None, description="List of destination sync modes supported by the connector"
    )
    authSpecification: Optional[AuthSpecification] = Field(None, description="deprecated, switching to advanced_auth instead")
    advanced_auth: Optional[AdvancedAuth] = Field(
        None,
        description="Additional and optional specification object to describe what an 'advanced' Auth flow would need to function.\n  - A connector should be able to fully function with the configuration as described by the ConnectorSpecification in a 'basic' mode.\n  - The 'advanced' mode provides easier UX for the user with UI improvements and automations. However, this requires further setup on the\n  server side by instance or workspace admins beforehand. The trade-off is that the user does not have to provide as many technical\n  inputs anymore and the auth process is faster and easier to complete.",
    )
    protocol_version: Optional[str] = Field(
        None,
        description="the Airbyte Protocol version supported by the connector. Protocol versioning uses SemVer. ",
    )


class AirbyteStateMessage(BaseModel):
    class Config:
        extra = Extra.allow

    type: Optional[AirbyteStateType] = None
    stream: Optional[AirbyteStreamState] = None
    global_: Optional[AirbyteGlobalState] = Field(None, alias="global")
    data: Optional[Dict[str, Any]] = Field(None, description="(Deprecated) the state data")


class AirbyteCatalog(BaseModel):
    class Config:
        extra = Extra.allow

    streams: List[AirbyteStream]


class ConfiguredAirbyteCatalog(BaseModel):
    class Config:
        extra = Extra.allow

    streams: List[ConfiguredAirbyteStream]


class AirbyteMessage(BaseModel):
    class Config:
        extra = Extra.allow

    type: Type = Field(..., description="Message type")
    log: Optional[AirbyteLogMessage] = Field(
        None,
        description="log message: any kind of logging you want the platform to know about.",
    )
    spec: Optional[ConnectorSpecification] = None
    connectionStatus: Optional[AirbyteConnectionStatus] = None
    catalog: Optional[AirbyteCatalog] = Field(None, description="catalog message: the catalog")
    record: Optional[AirbyteRecordMessage] = Field(None, description="record message: the record")
    state: Optional[AirbyteStateMessage] = Field(
        None,
        description="schema message: the state. Must be the last message produced. The platform uses this information",
    )
    trace: Optional[AirbyteTraceMessage] = Field(
        None,
        description="trace message: a message to communicate information about the status and performance of a connector",
    )
    control: Optional[AirbyteControlMessage] = Field(
        None,
        description="connector config message: a message to communicate an updated configuration from a connector that should be persisted",
    )


class AirbyteProtocol(BaseModel):
    airbyte_message: Optional[AirbyteMessage] = None
    configured_airbyte_catalog: Optional[ConfiguredAirbyteCatalog] = None
