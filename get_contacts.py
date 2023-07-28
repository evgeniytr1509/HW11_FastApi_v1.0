import requests

def get_contacts(base_url):
    url = f"{base_url}/contacts/"

    response = requests.get(url)

    if response.status_code == 200:
        contacts = response.json()
        return contacts
    else:
        return None

if __name__ == "__main__":
    base_url = "http://127.0.0.1:8000"  

    contacts = get_contacts(base_url)
    if contacts:
        print("Список всех контактов:")
        print(contacts)
    else:
        print("Ошибка при получении списка контактов.")