from backend.database.mongodb import customers_collection
from langchain_core.tools import tool


@tool
def get_customer(phone: str):
    """
    Find a customer using their phone number.
    """

    customer = customers_collection.find_one(
        {"phone": phone},
        {"_id": 0}
    )

    if not customer:
        return {
            "found": False,
            "message": "Customer not found."
        }

    return {
        "found": True,
        "customer": customer
    }


@tool
def create_customer(
    name: str,
    phone: str,
    address: str
):
    """
    Create a new customer.
    """

    existing = customers_collection.find_one(
        {"phone": phone}
    )

    if existing:
        return {
            "success": False,
            "message": "Customer already exists."
        }

    customer = {
        "name": name,
        "phone": phone,
        "address": address
    }

    result = customers_collection.insert_one(customer)

    return {
        "success": True,
        "customer_id": str(result.inserted_id),
        "customer": customer
    }