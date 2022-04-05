from pydantic import BaseModel, EmailStr , validator


class UserBase(BaseModel):
    email : EmailStr


class UserLogin(UserBase):
    password : str
        
    @validator('password')
    def password_len(cls, password):
        if len(password) < 6 :
            raise ValueError(f'La contraseña no debe ser menor de {6}')
        return password


class User(UserBase):
    id : int | None
    name : str | None
    google : bool | None
    is_activate : bool | None

    class Config:
        orm_mode = True


class VentasBase(BaseModel):
    tour_name : str
    cost : int 

class Ventas(VentasBase):
    id : int | None
    owner_id : int | None

    class Config:
        orm_mode = True 

