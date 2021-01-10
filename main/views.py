from django.shortcuts import render
from .models import User
import random

def index(request):
    return render(request, 'main/index.html')

def about(request):
    users = User.objects.all()
    return render(request, 'main/about.html', {'users' : users} )
