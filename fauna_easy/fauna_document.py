from typing import Generic, TypeVar
from faunadb.objects import Ref
from pydantic import BaseModel
from faunadb.objects import Ref

T = TypeVar('T')

class FaunaDocument(BaseModel, Generic[T]):
    ref: Ref
    ts: int
    data: T

    class Config:
        arbitrary_types_allowed = True
