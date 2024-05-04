import requests

def get_users():
    response = requests.get(f"https://jsonplaceholder.typicode.com/users")
    return response.json()

