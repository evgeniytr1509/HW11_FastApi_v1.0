import requests
import json

def add_contact(base_url, contact_data):
    url = f"{base_url}/contacts/"
    headers = {'Content-type': 'application/json'}
    json_data = json.dumps(contact_data)

    response = requests.post(url, json_data, headers=headers)

    if response.status_code == 200:
        new_contact = response.json()
        print("Контакт успешно добавлен:")
        print(new_contact)
    
    else:
        print(f"Ошибка: {response.status_code}, {response.text}")

if __name__ == "__main__":
    base_url = "http://127.0.0.1:8000"  

    new_contact_data = {
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@gmail.com",
        "phone": "123-456-7890",
        "birthday": "1990-01-01",
        "additional_data": {"address": "123 Main St"}
    }

    add_contact(base_url, new_contact_data)