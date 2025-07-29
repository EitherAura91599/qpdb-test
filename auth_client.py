import requests
import json
import random, string

BASE_URL = "http://localhost:8080"

def register(username, password, email):
    url = f"{BASE_URL}/register"
    payload = {
        "email": email,
        "username": username,
        "password": password
    }

    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print(simulated_api_requests)
    else:
        print("[✗] Registration failed:", response.json())


def login(username, password):
    url = f"{BASE_URL}/login"
    payload = {
        "username": username,
        "password": password
    }

    response = requests.post(url, json=payload)
    if response.status_code == 200:
        token = response.json().get("token")
        print("[✓] Login successful. JWT token:")
        print(token)
        return token
    else:
        print("[✗] Login failed:", response.json())
        return None

def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

def main():
    register(randomword(random.randint(5, 10)), randomword(random.randint(10, 20)), randomword(random.randint(5, 10)) +str("@email.com"))


if __name__ == "__main__":
    simulated_api_requests = 0
    while True:
        main()
        simulated_api_requests = simulated_api_requests + 1
