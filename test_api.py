import requests
BASE = "http://localhost:5000"
KEY = "codomax_2025_secret_key"

def test():
    print("GET /", requests.get(f"{BASE}/").json())
    print("GET /api/products", requests.get(f"{BASE}/api/products").json())
    print("POST without key should fail 401:", requests.post(f"{BASE}/api/products", json={"name":"Test"}).status_code)
    print("POST with key:", requests.post(f"{BASE}/api/products", json={"name":"Test Product","category":"Test","price":10,"stock":5}, headers={"X-API-KEY": KEY}).json())

if __name__ == "__main__":
    test()
