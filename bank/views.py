import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User
from .models  import Account



@csrf_exempt
def api_user(request):
    if request.method == "POST":
        try:
            req_data = json.loads(request.body)

            email = req_data.get("email")
            password = req_data.get("password")

            newUser = User.objects.create(email=email, password=password)

            print(newUser)
            return JsonResponse({"email": email, "password": password}, status=200)
        except:
            pass

@csrf_exempt
def api_Account(request):
    if request.method == 'POST':
        req_data = json.load(request.body)
        user_id = req_data.get('user_id')
        user_mail = req_data.get('email')
        balance = 0
        pin = req_data.get('pin')
        new_account = Account.save({'user_id': user_id,
                                    'email': user_mail,
                                    'balance': balance,
                                    'pin': pin
                                    })
        return JsonResponse(new_account)
