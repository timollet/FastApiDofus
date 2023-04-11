from pydantic import BaseModel

class user(BaseModel):
    id: int
    username: str