from db import db

products_col = db["products"]

def create_product(data):
    result = products_col.insert_one(data)
    return str(result.inserted_id)

def list_products(filters={}, limit=0, offset=0):
    query = {}
    if 'name' in filters:
        query['name'] = {"$regex": filters['name'], "$options": "i"}
    if 'size' in filters:
        query['sizes'] = filters['size']

    cursor = products_col.find(query).skip(offset).limit(limit)
    return [serialize_product(doc) for doc in cursor]

def serialize_product(doc):
    doc['_id'] = str(doc['_id'])
    return doc
