from django.shortcuts import render
from django.views import View
import json
from  django.http import JsonResponse
from django.contrib.auth.models import User

class registrationView(View):
    def get(self,request):
        return render(request,'authentication/register.html')
    
class UsernameValidationView(View):
    def post(self,request):
        data=json.loads(request.body)
        username=data['username']
        if not str(username).isalnum():
            return JsonResponse({'username_error': 'username should only contain alphanumeric characters'}, status=400)
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error': 'sorry username in use,choose another one '}, status=409)
        return JsonResponse({'username_valid':True})
    
    
class UsernameValidationView(View):
    def post(self,request):
        data=json.loads(request.body)
        email=data['email']
        if not str(email).isalnum():
            return JsonResponse({'email_error': 'email should only contain alphanumeric characters'}, status=400)
        if User.objects.filter(email=email).exists():
            return JsonResponse({'email_error': 'sorry email in use,choose another one '}, status=409)
        return JsonResponse({'email_valid':True})

# Create your views here.
