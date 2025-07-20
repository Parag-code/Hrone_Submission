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
# Visit your API documentation at:
👉 http://localhost:8000/docs
