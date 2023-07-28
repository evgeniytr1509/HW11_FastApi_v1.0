import requests

def get_contact_by_id(base_url, contact_id):
    url = f"{base_url}/contacts/{contact_id}"

    response = requests.get(url)

    if response.status_code == 200:
        contact = response.json()
        return contact
    elif response.status_code == 404:
        return None
    else:
        return None

if __name__ == "__main__":
    base_url = "http://127.0.0.1:8000"  
    contact_id = 1  # Заменить на конкретный идентификатор контакта
    contact = get_contact_by_id(base_url, contact_id)
    if contact:
        print("Контакт по идентификатору:")
        print(contact)
    else:
        print("Контакт с таким идентификатором не найден.")
