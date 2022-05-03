from pydantic import BaseModel

class DataModel(BaseModel):
    image: str

    def columns(self):
        return ["image"]

