from fauna_easy.fauna_document import FaunaDocument
from typing import List, Optional, Union
from pydantic import BaseModel
from faunadb.objects import Ref

class FaunaPaginateResponse(BaseModel):
    before: Optional[Ref]
    after: Optional[Ref]
    data: Union[List[Ref], List[FaunaDocument]]

    class Config:
        arbitrary_types_allowed = True
