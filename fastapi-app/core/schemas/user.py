from pydantic import BaseModel


class UserBase(BaseModel):
    __tablename__ = 'user'
    username: str
    email:str
    password: str
    age: int

class UserCreate(UserBase):
    pass

class UserRead(UserBase):
    id: int