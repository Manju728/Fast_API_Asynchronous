from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

class UserInDB(UserBase):
    id: int

class UserUpdate(UserBase):
    name: str
    email: str
    password: str

    class Config:
        orm_mode = True
