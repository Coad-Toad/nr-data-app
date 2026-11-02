import requests

def load_data(card):
    response = requests.get(card, timeout=10)
    response.raise_for_status()
    return response.json()