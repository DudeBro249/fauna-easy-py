from typing import Any, TypeVar

from faunadb import query as q
from faunadb.client import FaunaClient
from pydantic import BaseModel
import pydantic

from .store import FaunaEasyStore
from .fauna_document import FaunaDocument

T = TypeVar('T')

class FaunaEasyBaseModel:
    collection: str
    pydantic_basemodel: Any

    def __init__(self, collection: str, pydantic_basemodel: Any) -> None:
        self.collection = collection
        if not issubclass(pydantic_basemodel, BaseModel):
            raise Exception(
                f'pydantic_basemodel must be a subclass of pydantic.BaseModel'
            )

        self.pydantic_basemodel = pydantic_basemodel

    def _getFaunaClient(self) -> FaunaClient:
        fauna_secret: str = FaunaEasyStore().fauna_secret
        return FaunaClient(fauna_secret)

    def create(self, doc: dict, id: str = None) -> FaunaDocument[pydantic.BaseModel]:
        fauna_client = self._getFaunaClient()
        self.pydantic_basemodel(**doc)
        createdDocument = fauna_client.query(
            q.create(
                q.ref(
                    q.collection(
                        self.collection,
                    ),
                    id=id
                ) if id != None else q.collection(
                    self.collection,
                ),
                { 'data': doc },
            ),
        )

        return createdDocument


