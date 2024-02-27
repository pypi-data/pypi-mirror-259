"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
*!
Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022-2024)

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class StringArray(google.protobuf.message.Message):
    """Message types that are common to multiple protobufs."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATA_FIELD_NUMBER: builtins.int
    @property
    def data(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        data: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["data", b"data"]) -> None: ...

global___StringArray = StringArray

class DoubleArray(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATA_FIELD_NUMBER: builtins.int
    @property
    def data(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]: ...
    def __init__(
        self,
        *,
        data: collections.abc.Iterable[builtins.float] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["data", b"data"]) -> None: ...

global___DoubleArray = DoubleArray

class Int32Array(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATA_FIELD_NUMBER: builtins.int
    @property
    def data(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    def __init__(
        self,
        *,
        data: collections.abc.Iterable[builtins.int] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["data", b"data"]) -> None: ...

global___Int32Array = Int32Array

class Int64Array(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATA_FIELD_NUMBER: builtins.int
    @property
    def data(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    def __init__(
        self,
        *,
        data: collections.abc.Iterable[builtins.int] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["data", b"data"]) -> None: ...

global___Int64Array = Int64Array

class SInt64Array(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATA_FIELD_NUMBER: builtins.int
    @property
    def data(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    def __init__(
        self,
        *,
        data: collections.abc.Iterable[builtins.int] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["data", b"data"]) -> None: ...

global___SInt64Array = SInt64Array

class UInt32Array(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATA_FIELD_NUMBER: builtins.int
    @property
    def data(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    def __init__(
        self,
        *,
        data: collections.abc.Iterable[builtins.int] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["data", b"data"]) -> None: ...

global___UInt32Array = UInt32Array

class StringTriggerValue(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATA_FIELD_NUMBER: builtins.int
    data: builtins.str
    def __init__(
        self,
        *,
        data: builtins.str | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_data", b"_data", "data", b"data"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_data", b"_data", "data", b"data"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_data", b"_data"]) -> typing_extensions.Literal["data"] | None: ...

global___StringTriggerValue = StringTriggerValue

class FileURLsRequest(google.protobuf.message.Message):
    """NOTE: The FileURLsRequest, FileURLs, and FileURLsResponse message types
    must remain stable as some external services rely on them to support
    `st.file_uploader`. These types aren't completely set in stone, but changing
    them requires a good amount of effort so should be avoided if possible.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REQUEST_ID_FIELD_NUMBER: builtins.int
    FILE_NAMES_FIELD_NUMBER: builtins.int
    SESSION_ID_FIELD_NUMBER: builtins.int
    request_id: builtins.str
    @property
    def file_names(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    session_id: builtins.str
    def __init__(
        self,
        *,
        request_id: builtins.str = ...,
        file_names: collections.abc.Iterable[builtins.str] | None = ...,
        session_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["file_names", b"file_names", "request_id", b"request_id", "session_id", b"session_id"]) -> None: ...

global___FileURLsRequest = FileURLsRequest

class FileURLs(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FILE_ID_FIELD_NUMBER: builtins.int
    UPLOAD_URL_FIELD_NUMBER: builtins.int
    DELETE_URL_FIELD_NUMBER: builtins.int
    file_id: builtins.str
    upload_url: builtins.str
    delete_url: builtins.str
    def __init__(
        self,
        *,
        file_id: builtins.str = ...,
        upload_url: builtins.str = ...,
        delete_url: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["delete_url", b"delete_url", "file_id", b"file_id", "upload_url", b"upload_url"]) -> None: ...

global___FileURLs = FileURLs

class FileURLsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESPONSE_ID_FIELD_NUMBER: builtins.int
    FILE_URLS_FIELD_NUMBER: builtins.int
    ERROR_MSG_FIELD_NUMBER: builtins.int
    response_id: builtins.str
    @property
    def file_urls(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___FileURLs]: ...
    error_msg: builtins.str
    def __init__(
        self,
        *,
        response_id: builtins.str = ...,
        file_urls: collections.abc.Iterable[global___FileURLs] | None = ...,
        error_msg: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["error_msg", b"error_msg", "file_urls", b"file_urls", "response_id", b"response_id"]) -> None: ...

global___FileURLsResponse = FileURLsResponse

class UploadedFileInfo(google.protobuf.message.Message):
    """Information on a file uploaded via the file_uploader widget."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    SIZE_FIELD_NUMBER: builtins.int
    FILE_ID_FIELD_NUMBER: builtins.int
    FILE_URLS_FIELD_NUMBER: builtins.int
    id: builtins.int
    """DEPRECATED."""
    name: builtins.str
    size: builtins.int
    """The size of this file in bytes."""
    file_id: builtins.str
    """ID that can be used to retrieve a file."""
    @property
    def file_urls(self) -> global___FileURLs:
        """Metadata containing information about file_urls."""
    def __init__(
        self,
        *,
        id: builtins.int = ...,
        name: builtins.str = ...,
        size: builtins.int = ...,
        file_id: builtins.str = ...,
        file_urls: global___FileURLs | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["file_urls", b"file_urls"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["file_id", b"file_id", "file_urls", b"file_urls", "id", b"id", "name", b"name", "size", b"size"]) -> None: ...

global___UploadedFileInfo = UploadedFileInfo

class FileUploaderState(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MAX_FILE_ID_FIELD_NUMBER: builtins.int
    UPLOADED_FILE_INFO_FIELD_NUMBER: builtins.int
    max_file_id: builtins.int
    """DEPRECATED"""
    @property
    def uploaded_file_info(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___UploadedFileInfo]: ...
    def __init__(
        self,
        *,
        max_file_id: builtins.int = ...,
        uploaded_file_info: collections.abc.Iterable[global___UploadedFileInfo] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["max_file_id", b"max_file_id", "uploaded_file_info", b"uploaded_file_info"]) -> None: ...

global___FileUploaderState = FileUploaderState
