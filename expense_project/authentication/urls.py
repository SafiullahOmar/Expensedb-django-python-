from .views import registrationView,UsernameValidationView
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('register',registrationView.as_view(),name="register"),
    path('validation-username',csrf_exempt(UsernameValidationView.as_view()),name="validation-username")
]
