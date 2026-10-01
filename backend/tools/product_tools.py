from backend.database.mongodb import products_collection
from langchain_core.tools import tool


@tool
def search_products(query: str):
    """
    Search products available in the store.
    Use this when the customer asks about products,
    prices, availability, or wants to buy something.
    """

    products = list(
        products_collection.find(
            {
                "$or": [
                    {"name": {"$regex": query, "$options": "i"}},
                    {"category": {"$regex": query, "$options": "i"}}
                ],
                "available": True
            },
            {
                "_id": 0
            }
        ).limit(10)
    )

    if not products:
        return f"No products found for '{query}'."

    return products