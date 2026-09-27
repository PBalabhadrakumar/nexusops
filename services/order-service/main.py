from fastapi import FastAPI
import os
import requests

app = FastAPI(title="Order Service", version="1.0.0")

USER_SERVICE_URL = os.getenv("USER_SERVICE_URL", "http://user-service:8001")
PRODUCT_SERVICE_URL = os.getenv("PRODUCT_SERVICE_URL", "http://product-service:8002")

@app.get("/")
def read_root():
    return {"service": "Order Service", "status": "Healthy"}

@app.post("/orders/")
def create_order(user_id: int, product_id: int, quantity: int):
    try:
        user_res = requests.get(f"{USER_SERVICE_URL}/users/{user_id}").json()
        prod_res = requests.get(f"{PRODUCT_SERVICE_URL}/products/{product_id}").json()
    except Exception as e:
        return {"error": "Inter-service communication failed", "details": str(e)}

    return {
        "order_id": 5001,
        "user": user_res,
        "product": prod_res,
        "quantity": quantity,
        "total_price": prod_res.get("price", 0) * quantity,
        "status": "CREATED"
    }
