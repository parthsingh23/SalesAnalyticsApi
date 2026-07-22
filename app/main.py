from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI(
    title="Sales Analytics API",
    description="Backend API for Sales Analytics Dashboard",
    version="1.0.0",
)


@app.get("/")
def root():
    return {"message": "Welcome to Sales Analytics API"}


@app.get("/about")
def about():
    return {"project": "Sales Analytics API", "developer": "Parth Singh"}


@app.get("/health")
def health():
    return {"status": "healthy"}


products = {
    1: {"name": "Mouse", "price": 25.99, "category": "Electronics"},
    2: {"name": "Shoes", "price": 79.99, "category": "Footwear"},
    3: {"name": "Mug", "price": 12.50, "category": "Kitchen"},
    4: {"name": "Notebook", "price": 5.99, "category": "Stationery"},
    5: {"name": "Speaker", "price": 49.99, "category": "Electronics"},
}


@app.get("/get-product-details")
def get_product_name(name: str):
    for product_id in products:
        if products[product_id]["name"] == name:
            return products[product_id]
    return {"Data": "Product Not Found"}

@app.get("/get-product-category")
def product_category(name: str):
    for product_id in products:
        if products[product_id]["name"] == name:
            return products[product_id]["category"]
    return {"Data": "Product Not Found"}

@app.get("/products-by-id-and-category")
def get_product(product_id: int, cat: Optional[str] = None):
    if product_id in products:
        product = products[product_id]
        if cat is None: 
            return product['name']
        else:
            if product['category'] == cat:
                return product['name']
    return {"Data": "Invalid ID or Category"}     


@app.get("/sales")
def get_sales(year: int, month: int, category: str = "All"):
    return {
        "year": year, "month": month, "category": category
    }