from enum import Enum
from typing import Any, BinaryIO, Optional, Union
from pydantic import BaseModel

class HttpObjectType(Enum):
    REQUEST = 'REQUEST'
    RESPONSE = 'RESPONSE'
    
class LogType(Enum):
    FUNCTION_CALL = 'FUNCTION_CALL'
    HTTP_OBJECT = 'HTTP_OBJECT'

class StradaError(BaseModel):
    errorCode: int
    statusCode: int
    message: str

    def __getitem__(self, item):
        return getattr(self, item)   

class StradaResponse(BaseModel):
    error: Optional[StradaError] = None
    success: bool
    data: Optional[Any] = None

    def __getitem__(self, item):
        return getattr(self, item)

class StradaHttpResponse(StradaResponse):
    status_code: int
    headers: dict

class StradaFunction():
    def __init__(self, function_name: str):
        self.function_name = function_name

    def execute(self, **kwargs):
        raise NotImplementedError


FileContent = Union[bytes, BinaryIO]
FileTuple = tuple[str, FileContent, Union[str, None]]
FilesDict = dict[str, FileTuple]