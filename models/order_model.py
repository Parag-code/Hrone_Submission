from db import db

orders_col = db["orders"]

def create_order(data):
    result = orders_col.insert_one(data)
    return str(result.inserted_id)

def get_orders_by_user(user_id, limit=0, offset=0):
    cursor = orders_col.find({"user_id": user_id}).skip(offset).limit(limit)
    return [serialize_order(doc) for doc in cursor]

def serialize_order(doc):
    doc['_id'] = str(doc['_id'])
    return doc
