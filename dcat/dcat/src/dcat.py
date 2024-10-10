from pydantic import BaseModel


class DCATBase(BaseModel):
    def __init__(self):
        pass

    def push(self, url=None):
        pass

    def pull(self, url=None):
        pass


class DCATMinimum(DCATBase):
    pass


class DCATExtended(DCATMinimum):
    pass
