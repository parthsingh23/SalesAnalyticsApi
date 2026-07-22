from fastapi import FastAPI, Path
from typing import Optional
from app.models import Product # Importing our base model

app = FastAPI(
    title="Sales Analytics API",
    description="Backend API for Sales Analytics Dashboard",
    version="1.0.0",
)


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


@app.get("/get-product/{product_id}")
def get_product_details(product_id: int = Path(description="ID of the product you want to view")):
    if product_id in products:
        return products[product_id]
    return {"Message":"ID not found"}

@app.get("/get-product-by-name/{name}")
def get_product_by_name(name: str = Path(description="name of the product you want to view")):
    for product in products.values():
        if product["name"] == name:
            return product
    return {"Message":"Product Not Found"}

@app.get("/products-by-id-and-category/")
def get_product(product_id: int, cat: Optional[str] = None):
    if product_id in products:
        product = products[product_id]
        if cat is None: 
            return product['name']
        else:
            if product['category'] == cat:
                return product['name']
    return {"Data": "Invalid ID or Category"}     


@app.post("/create-new-product/{product_id}")
def create_new_product(product_id: int, productDetail: Product):
    if product_id in products:
        return {"Error": "Product already Exists"}

    products[product_id] = productDetail.model_dump()
    return products[product_id]