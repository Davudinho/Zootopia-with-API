import requests

API_URL = "https://api.api-ninjas.com/v1/animals?name={}"
API_KEY = "i/8+R/6Kq4v6HlSxWVO4tg==79f5TT9lVpDhib1d"  # 🔐 besser in .env auslagern

def fetch_data(animal_name):
    """
    Fetches the animal data for 'animal_name' from the API.
    Returns:
        A list of animal dictionaries (or an empty list if none found).
    """
    url = API_URL.format(animal_name)
    headers = {"X-Api-Key": API_KEY}

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # löst Fehler bei 4xx / 5xx aus

        data = response.json()
        if not data:
            print(f"❌ No animal found for '{animal_name}'.")
            return []

        return data

    except requests.exceptions.RequestException as e:
        print("❌ API Error:", e)
        return []
