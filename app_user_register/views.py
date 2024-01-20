from django.shortcuts import render
from .models import User

def home(request):
    return render(request, "users/home.html")

def users(request):
    #New User Object and saving into database
    new_user = User()
    new_user.name = request.POST.get("nameInput")
    new_user.age = request.POST.get("ageInput")
    new_user.save()

    #Show users in new page
    users = {
        "users": User.objects.all()
    }

    return render(request, 'users/users.html',users)