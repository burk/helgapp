from django.shortcuts import render
from django.contrib.auth.models import User

def register_form(request):
    return render(request, 'registration/sign_up.html')

def register(request):
    User.objects.create_user(request.username, request.password)
    return render(request, 'registration/login.html')
