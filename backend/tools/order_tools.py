from backend.database.mongodb import (
    products_collection,
    orders_collection
)

from langchain_core.tools import tool
from langgraph.types import interrupt

from datetime import datetime, timezone
import uuid


@tool
def calculate_order(items: list):
    """
    Calculate the total price of an order.

    Example:
    [
        {"name": "Paneer Pizza", "quantity": 2},
        {"name": "Coke", "quantity": 1}
    ]
    """

    calculated_items = []
    total = 0

    for item in items:
        product = products_collection.find_one(
            {
                "name": {
                    "$regex": f"^{item['name']}$",
                    "$options": "i"
                },
                "available": True
            }
        )

        if not product:
            return {
                "success": False,
                "message": f"Product '{item['name']}' not found."
            }

        quantity = int(item["quantity"])

        if quantity <= 0:
            return {
                "success": False,
                "message": "Quantity must be greater than zero."
            }

        item_total = product["price"] * quantity

        calculated_items.append({
            "name": product["name"],
            "quantity": quantity,
            "price": product["price"],
            "item_total": item_total
        })

        total += item_total

    return {
        "success": True,
        "items": calculated_items,
        "total": total
    }


@tool
def confirm_order(items: list, total: float):
    """
    Ask the customer for explicit confirmation before
    placing an order. This pauses the LangGraph workflow.
    """

    confirmation = interrupt({
        "type": "order_confirmation",
        "message": (
            f"Your order total is ₹{total}. "
            "Would you like me to place the order?"
        ),
        "items": items,
        "total": total
    })

    answer = str(confirmation).strip().lower()

    positive_answers = [
        "yes",
        "y",
        "yeah",
        "yep",
        "sure",
        "confirm",
        "confirmed",
        "place it",
        "place the order",
        "go ahead"
    ]

    if answer in positive_answers:
        return {
            "confirmed": True,
            "items": items,
            "total": total
        }

    return {
        "confirmed": False,
        "message": "Order was not confirmed."
    }


@tool
def create_order(
    items: list,
    total: float,
    customer_id: str = "guest"
):
    """
    Create the order in MongoDB after customer confirmation.
    """

    order_id = "ORD-" + uuid.uuid4().hex[:8].upper()

    order = {
        "order_id": order_id,
        "customer_id": customer_id,
        "items": items,
        "total": total,
        "status": "confirmed",
        "created_at": datetime.now(timezone.utc)
    }

    orders_collection.insert_one(order)

    return {
        "success": True,
        "order_id": order_id,
        "status": "confirmed",
        "total": total
    }


@tool
def get_order_status(order_id: str):
    """
    Get the status of an order using its order ID.
    """

    order = orders_collection.find_one(
        {"order_id": order_id},
        {"_id": 0}
    )

    if not order:
        return {
            "success": False,
            "message": "Order not found."
        }

    return order


@tool
def get_order_history(customer_id: str):
    """
    Get the recent order history of a customer.
    """

    orders = list(
        orders_collection.find(
            {"customer_id": customer_id},
            {"_id": 0}
        )
        .sort("created_at", -1)
        .limit(10)
    )

    return orders