class FaunaEasyStore:
    _instance = None

    def __new__(cls, fauna_secret: str = None):
        if cls._instance is None:
            cls._instance = super(FaunaEasyStore, cls).__new__(cls)
            cls._instance.fauna_secret = fauna_secret
        return cls._instance
