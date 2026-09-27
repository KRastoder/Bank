import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User


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
