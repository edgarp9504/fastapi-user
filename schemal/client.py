from pydantic import BaseModel, EmailStr


class Client(BaseModel):
    id : int | None
    name : str
    email : EmailStr
    phone : int | None

    class Config:
        orm_mode = True
