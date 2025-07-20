# HRone Backend Intern Task - FastAPI + MongoDB

This project is a backend application built using **FastAPI** that simulates basic e-commerce functionality, including product and order management with MongoDB.

---

## 🚀 Features

- ✅ Create Product  
- ✅ List Products with Filters (name, price range, category)  
- ✅ Create Order  
- ✅ List Orders by User  

---

## 🛠 Tech Stack

- Python 3.10+
- FastAPI
- MongoDB (Atlas - Free Tier)
- Pymongo

---

## ⚙️ MongoDB Configuration

Update your `config.py` with:

```python
MONGO_URI = "your_mongo_connection_string"
DB_NAME = "your_database_name"
```
## 💻 Running Locally

```bash
# Install dependencies
pip install -r requirements.txt
```

# Start the server
```bash
uvicorn main:app --reload
```

## 📡 API Endpoints

### 🔹 Product Routes

#### `POST /products`  
Create a new product  
**Request Body (JSON):**
```json
{
  "name": "Laptop",
  "price": 49999,
  "category": "Electronics"
}
```
GET /products
Get list of products with optional query parameters:

- name (string)

- min_price (integer)

- max_price (integer)

- category (string)

Example:

``` bash
/products?category=Electronics&min_price=10000&max_price=60000
```
🔹 Order Routes
  POST /orders
  Create a new order
  Request Body (JSON):
  ```bash 
{
  "user_id": "u123",
  "product_ids": ["64a1e123...", "64a1e456..."]
}
```
GET /orders/{user_id}
Get all orders placed by a specific user.
```bash
/orders/u123
```
