from .store import FaunaEasyStore

def use(fauna_secret: str):
    FaunaEasyStore(fauna_secret=fauna_secret)
