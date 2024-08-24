import json
from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.http.request import HttpRequest
from django.conf import settings

from utils.paystack import create_customer, create_dva




import hmac
import hashlib

# Create your views here.



# {'data': {'authorizations': [],
#           'createdAt': '2024-08-24T13:20:43.453Z',
#           'customer_code': 'CUS_udz6t9i1z30i4xm',
#           'domain': 'test',
#           'email': 'haresa5572@daypey.com',
#           'first_name': 'Wisdom',
#           'id': 182482052,
#           'identifications': None,
#           'identified': False,
#           'integration': 1228532,
#           'last_name': 'Dakoh',
#           'metadata': {},
#           'phone': '+2347098556732',
#           'risk_action': 'default',
#           'subscriptions': [],
#           'transactions': [],
#           'updatedAt': '2024-08-24T13:20:43.453Z'},
#  'message': 'Customer created',
#  'status': True}



def webhook(request: HttpRequest) -> JsonResponse:

    if request.method == 'POST':

        secret_key: str = settings.PAYSTACK_SECRET_KEY

        signature = request.headers.get('x-paystack-signature')

        hash_signature = hmac.new(secret_key.encode('utf-8'), request.body, hashlib.sha512).hexdigest()

        if hash_signature != signature:
            return JsonResponse({'message': 'Invalid signature'}, status=400)
        

        event = json.loads(request.body)



        if event.get('event') == 'charge.success':

            # Confirm with the charge was s dedicated account charge
            # "channel": "dedicated_nuban",

            # Get the user's email that was used to create the dedicated account


            user_email= event.get("date").get("customer").get("email")

            # user = fetchone(User, email=user_reference.get("email"))

            user = User.objects.get(email=user_email)

            user.wallet_balance += int(event.get("data").get("amount")) / 100

            user.save()

        else: 
            print("Unhandled Event", event)


        return JsonResponse({'message': 'Webhook received'}, status=200)



    print("The webhook has been called")
    return JsonResponse({'message': 'The webhook has been called & i love eating'}, status=200)




