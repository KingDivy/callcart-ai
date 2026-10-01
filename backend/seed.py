from backend.database.mongodb import (
    products_collection,
    customers_collection
)


products = [
    {
        "name": "Paneer Pizza",
        "category": "Pizza",
        "price": 250,
        "available": True
    },
    {
        "name": "Margherita Pizza",
        "category": "Pizza",
        "price": 220,
        "available": True
    },
    {
        "name": "Farmhouse Pizza",
        "category": "Pizza",
        "price": 280,
        "available": True
    },
    {
        "name": "Veg Burger",
        "category": "Burger",
        "price": 150,
        "available": True
    },
    {
        "name": "Chicken Burger",
        "category": "Burger",
        "price": 180,
        "available": True
    },
    {
        "name": "Coke",
        "category": "Beverage",
        "price": 50,
        "available": True
    },
    {
        "name": "Fries",
        "category": "Sides",
        "price": 100,
        "available": True
    }
]


def seed_database():

    products_collection.delete_many({})

    result = products_collection.insert_many(products)

    print(
        f"Inserted {len(result.inserted_ids)} products."
    )


if __name__ == "__main__":
    seed_database()