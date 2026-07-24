from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException

from app.models import Product, UpdateProduct # Importing our base model
from app.models import Item, UserIn, UserBase, UserOut
from app.database import create_db_and_tables

# app = FastAPI(
#     title="Sales Analytics API",
#     description="Backend API for Sales Analytics Dashboard",
#     version="1.0.0",
# )

@asynccontextmanager
async def startup(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=startup)


products = {
    1: {"name": "Mouse", "price": 25.99, "stock": 10,  "category": "Electronics"},
    2: {"name": "Shoes", "price": 79.99, "stock": 20, "category": "Footwear"},
    3: {"name": "Mug", "price": 12.50, "stock": 45, "category": "Kitchen"},
    4: {"name": "Notebook", "price": 5.99, "stock": 35, "category": "Stationery"},
    5: {"name": "Speaker", "price": 49.99, "stock": 80, "category": "Electronics"},
}

@app.get("/")
def root():
    return {"message": "Welcome to Sales Analytics API"}


@app.get("/about")
def about():
    return {"project": "Sales Analytics API", "developer": "Parth Singh"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/products/", response_model=dict[int, Product])
def get_products(name: str | None = None):
    if name is None:
        return products

    for product in products.values():
        if product["name"].lower() == name.lower():
            return product

    raise HTTPException(
        status_code=404,
        detail="Product Not Found"
    )

@app.get("/products/{product_id}", response_model=Product)
def get_product(product_id: int):
    if product_id not in products:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )
    return products[product_id]

@app.post("/products/{product_id}", response_model=Product, status_code=201)
def create_product(product_id: int, product: Product):
    if product_id in products:
        raise HTTPException(
            status_code=409,
            detail="Product already exist"
        )
    products[product_id] = product.model_dump()
    return products[product_id]


# @app.post("/items/", response_model = Item)
# def create_item(item: Item):
#     return item 

# @app.post("/user/", response_model=UserOut)
# def add_user(user: UserIn):
#     return user

# @app.get("/products", response_model = dict[int, Product], status_code=201)
# def get_all_products():
#     return products


@app.put("/products/{product_id}", response_model= Product)
def update_product(product_id: int, product: UpdateProduct):
    if product_id not in products:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )
    products[product_id].update(
        product.model_dump(exclude_unset=True)
    )

    return products[product_id]

@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    if product_id not in products:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )
    del products[product_id]

    return {"Message":"Product deleted Sucesfully"}