import requests

BASE = "http://127.0.0.1:7070"

def test_analyze():
    data = {"text": "Hi I am Li Hua, phone 123-456-7890, email li@example.com, live in Baltimore."}
    resp = requests.post(f"{BASE}/analyze", json=data)
    print("=== /analyze ===")
    print(resp.json())

def test_sanitize():
    data = {"text": "My card 4111 1111 1111 1111, call me at 555-123-4567."}
    resp = requests.post(f"{BASE}/sanitize", json=data)
    print("=== /sanitize ===")
    print(resp.json())

if __name__ == "__main__":
    test_analyze()
    test_sanitize()
