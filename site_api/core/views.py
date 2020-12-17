from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .serializers import *
import json

def all_users(request):
    users = Users.objects.all()
    serialized_users = CoreSerializer(users).all_users
    return JsonResponse(data=serialized_users, status=200)

def all_quotes(request):
    quotes = Quotes.objects.all()
    serialized_quotes = CoreSerializer(quotes).all_quotes
    return JsonResponse(data=serialized_quotes, status=200)