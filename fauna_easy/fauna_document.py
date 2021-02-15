from typing import Any, Generic, TypeVar
from pydantic import BaseModel

T = TypeVar('T')

class FaunaDocument(BaseModel, Generic[T]):
    ref: Any
    ts: int
    data: T
