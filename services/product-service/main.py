from fastapi import FastAPI

app = FastAPI(title="Product Service", version="1.0.0")

@app.get("/")
def read_root():
    return {"service": "Product Service", "status": "Healthy"}

@app.get("/products/{product_id}")
def get_product(product_id: int):
    return {"product_id": product_id, "name": f"Product {product_id}", "price": 99.99}
