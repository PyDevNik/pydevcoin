from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str
    balance: float = 0.0
    token: str