import os
import requests
from dotenv import load_dotenv
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(category=InsecureRequestWarning)

load_dotenv()
tenant_id = os.getenv("tenant_id")
client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")
resource = os.getenv("resource")

def get_access_token():
    session = requests.Session()
    retries = Retry(total=5,             
                    backoff_factor=1,     
                    status_forcelist=[500, 502, 503, 504],  
                    allowed_methods=["POST"])    
    adapter = HTTPAdapter(max_retries=retries)
    session.mount('https://', adapter)
    session.mount('http://', adapter)
    url = f'https://login.microsoftonline.com:443/{tenant_id}/oauth2/token'
    print(f"URL: {url}")
    data = {
        'client_id': client_id,
        'client_secret': client_secret,
        'resource': resource,
        'grant_type': 'client_credentials',
    }
    response = session.post(url, data=data, verify=False)
    access_token = response.json().get('access_token')

    return access_token


