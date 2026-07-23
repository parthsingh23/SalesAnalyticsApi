from pydantic import BaseModel, EmailStr, Field

class Product(BaseModel):
    name: str = Field(min_length=2, max_length=100, description="Product Name")
    price: float = Field(gt=0, description="Product Price")
    stock: int = Field(ge=0, description="Available Stock")
    category: str = Field(min_length=2, max_length=50, description="Product Category")

class UpdateProduct(BaseModel):
    name: str | None = Field(default=None, min_length=2, max_length=100)
    price: float | None = Field(default=None, gt=0)
    stock: int | None = Field(default=None, ge=0)
    category: str | None = Field(default=None, min_length=2, max_length=50)



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

