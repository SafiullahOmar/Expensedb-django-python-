from django.shortcuts import render
from django.views import View

class registrationView(View):
    def get(self,request):
        return render(request,'authentication/register.html')

# Create your views here.
