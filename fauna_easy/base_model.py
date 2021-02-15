from typing import Any

from faunadb import query as q
from faunadb.client import FaunaClient
from pydantic import BaseModel

from .store import FaunaEasyStore
from .fauna_document import FaunaDocument

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

    def create(self, doc: dict, id: str = None) -> FaunaDocument[dict]:
        fauna_client = self._getFaunaClient()
        self.pydantic_basemodel(**doc)
        created_document = fauna_client.query(
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

        return FaunaDocument(**created_document)
    
    def delete(self, id: str) -> FaunaDocument[dict]:
        fauna_client = self._getFaunaClient()
        deleted_document = fauna_client.query(
            q.delete(
                q.ref(
                    q.collection(
                        self.collection,
                    ),
                    id=id
                )
            ),
        )

        return FaunaDocument(**deleted_document)

    
    def update(self, doc: dict, id: str) -> FaunaDocument[dict]:
        fauna_client = self._getFaunaClient()
        updated_document = fauna_client.query(
            q.update(
                q.ref(
                    q.collection(
                        self.collection,
                    ),
                    id=id
                ),
                { 'data': doc },
            ),
        )

        return FaunaDocument(**updated_document)
    

    def find_by_id(self, id: str) -> FaunaDocument[dict]:
        fauna_client = self._getFaunaClient()
        document: FaunaDocument[dict] = fauna_client.query(
            q.get(
                q.ref(
                    q.collection(self.collection),
                    id,
                )
            )
        )

        return FaunaDocument(**document)
