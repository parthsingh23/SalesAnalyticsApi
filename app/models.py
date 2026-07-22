from pydantic import BaseModel, EmailStr

class Product(BaseModel):
    name: str
    price: float
    stock: int
    category: str

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []

class UserBase(BaseModel):
    name: str
    email: EmailStr
    full_name: str | None = None


class UserIn(UserBase):
    passwd: str

class UserOut(UserBase):
    pass