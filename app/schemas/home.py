from pydantic import BaseModel


class Home(BaseModel):
    name: str
    api_version: str
    model_version: str
