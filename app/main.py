from fastapi import FastAPI, HTTPException
from app.models import Product # Importing our base model
from app.models import Item, UserIn, UserBase, UserOut

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
def get_product_details(product_id: int):
    if product_id in products:
        return products[product_id]
    raise HTTPException(
        status_code=404,
        detail="Product Not found."
    )

@app.get("/get-product-by-name/{name}")
def get_product_by_name(name: str):
    for product in products.values():
        if product["name"] == name:
            return product
    raise HTTPException(
        status_code=404,
        detail="Product Not found."
    )

@app.get("/products-by-id-and-category/")
def get_product(product_id: int, cat: str | None = None):
    if product_id in products:
        product = products[product_id]
        if cat is None: 
            return product['name']
        else:
            if product['category'] == cat:
                return product['name']
    raise HTTPException(
        status_code=400,
        detail="Invalid ID or category."
    )    


@app.post("/create-new-product/{product_id}", response_model=Product, status_code=201)
def create_new_product(product_id: int, productDetail: Product):
    if product_id in products:
        # return {"Error": "Product already Exists"}
        raise HTTPException(
            status_code=409,
            detail="Product already Exists."
        )
    products[product_id] = productDetail.model_dump()
    return products[product_id]


@app.post("/items/", response_model = Item)
def create_item(item: Item):
    return item 

@app.post("/user/", response_model=UserOut)
def add_user(user: UserIn):
    return user