from fastapi import FastAPI
from typing import List, Optional
from pydantic import BaseModel
import uvicorn

# Pydantic model for product response
class ProductResponse(BaseModel):
    id: int
    name: str
    available: bool

# Product class for internal data representation
class Product:
    def __init__(self, id: int, name: str, available: bool):
        self.id = id
        self.name = name
        self.available = available

# Sample products
products = [
    Product(1, "Jolly Jester Clown Wig", True),
    Product(2, "Bozo the Clown Nose", False),
    Product(3, "Circus Performer Clown Shoes", True),
    Product(4, "Red Balloon Animal Kit", True),
    Product(5, "Funny Clown Face Paint Set", True),
    Product(6, "Mini Clown Horn", False),
    Product(7, "Rainbow Clown Costume", True),
    Product(8, "Clown Magician Hat", True),
    Product(9, "Giggles the Clown Plush Doll", True),
    Product(10, "Clown Comedy Seltzer Bottle", False)
]

# FastAPI app initialization
app = FastAPI()

@app.get("/products", response_model=List[ProductResponse])
def get_products(available: Optional[bool] = None):
    # If 'available' query param is provided, filter products by availability
    filtered_products = products if available is None else [product for product in products if product.available == available]
    
    # Return products as list of Pydantic model instances
    return [ProductResponse(**product.__dict__) for product in filtered_products]

@app.get("/")
def main():
    return {"message": "Hello from store-api!"}

if __name__ == "__main__":
   uvicorn.run(app, host="0.0.0.0", port=8000)
   #main() # to run using command line `uv run uvicorn hello:app --port 8000`
