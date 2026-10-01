from pymongo import MongoClient
from backend.config import MONGODB_URI


client = MongoClient(
    MONGODB_URI,
    serverSelectionTimeoutMS=10000
)

db = client["callcart"]

products_collection = db["products"]
customers_collection = db["customers"]
orders_collection = db["orders"]


def test_connection():
    try:
        client.admin.command("ping")
        print("MongoDB connected successfully!")
    except Exception as e:
        print("MongoDB connection failed!")
        print(e)