import requests

def get_animal_info(animal_name):
    url = f"https://api.api-ninjas.com/v1/animals?name={animal_name}"
    api_key = "i/8+R/6Kq4v6HlSxWVO4tg==79f5TT9lVpDhib1d"

    headers = {"X-Api-Key": api_key}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if data:
            print(f"✅ Found information about {animal_name}:")
            print(data[0])
        else:
            print(f"⚠️ No information found for '{animal_name}'.")
    else:
        print(f"❌ Error {response.status_code}: {response.text}")


get_animal_info("fox")
