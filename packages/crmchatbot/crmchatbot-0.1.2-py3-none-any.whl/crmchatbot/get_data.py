import requests
from dotenv import load_dotenv
from .access_token import get_access_token
load_dotenv()

def get_data(input):

    access_token = get_access_token()
    entity_name = input.lstrip('\n')
    print(f"here is entity {entity_name}")
    url2 = f"https://orgd7246cd1.api.crm4.dynamics.com/api/data/v9.2/{entity_name}"

    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json',
        'OData-MaxVersion': '4.0',
        'OData-Version': '4.0',
    }

    response = requests.get(url2, headers=headers)

    if response.status_code == 200:
        record = response.json()
        if record["value"] == [''] or not record["value"]:
            return False
        return record
    else:
        print(f"Error: {response.status_code}")
    
   
