from fastapi import FastAPI, Request, Query
from typing import Optional
from models.product_model import create_product, list_products
from models.order_model import create_order, get_orders_by_user

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to HRone FastAPI"}

@app.post("/products", status_code=201)
async def add_product(request: Request):
    data = await request.json()
    product_id = create_product(data)
    return {"message": "Product created", "product_id": product_id}

@app.get("/products")
def get_products(
    name: Optional[str] = None,
    size: Optional[str] = None,
    limit: Optional[int] = 0,
    offset: Optional[int] = 0
):
    filters = {}
    if name:
        filters['name'] = name
    if size:
        filters['size'] = size
    products = list_products(filters, limit, offset)
    return products

@app.post("/orders", status_code=201)
async def add_order(request: Request):
    data = await request.json()
    order_id = create_order(data)
    return {"message": "Order created", "order_id": order_id}

@app.get("/orders/{user_id}")
def get_user_orders(user_id: str, limit: int = 0, offset: int = 0):
    orders = get_orders_by_user(user_id, limit, offset)
    return orders
