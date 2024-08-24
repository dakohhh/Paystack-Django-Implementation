import requests
from django.conf import settings
from pprint import pprint





def create_customer(email:str, first_name:str, last_name:str, phone:str) -> dict:

    url = 'https://api.paystack.co/customer'

    headers = {
        "Authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}",
    }

    details = {

        "email": email,
        "first_name": first_name,
        "last_name": last_name,
        "phone": phone,
    }

    result = requests.post(url, data=details, headers=headers)

    pprint(result.json())
    


def create_dva(customer_id:int) -> dict:

    url = 'https://api.paystack.co/dedicated_account'

    headers = {
        "Authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}",
    }

    details = {
        "customer": customer_id,
        "preferred_bank": "test-bank",

    }

    result = requests.post(url, data=details, headers=headers)

    pprint(result.json())
