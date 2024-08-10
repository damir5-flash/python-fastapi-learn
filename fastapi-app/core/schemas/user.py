from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    username: str
    email: EmailStr
    password: str
    age: int

class UserCreate(UserBase):
    pass

class UserRead(UserBase):
    id: int
