from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from main.models import FoodCategory, Food


def index_view(request: HttpRequest):

    categories = FoodCategory.objects.all()

    context = {
        "categories": categories
    }

    return render(request, "index.html", context=context)


def category_detail(request: HttpRequest, pk):
    category = FoodCategory.objects.get(pk=pk)
    
    context = {
        "category": category
    }

    return render(request, "category-detail.html", context=context)
    


def login_view(request: HttpRequest):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if not user:
            return redirect("login")
        
        login(request, user)
        return redirect("index")

    return render(request, "login.html")


def logout_view(request: HttpRequest):
    logout(request)
    return redirect("login")


def signup_view(request: HttpRequest):

    if request.method == "POST":
        first_name = request.POST.get("first_name", None)
        last_name = request.POST.get("last_name", None)
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        login(request, user)
        return redirect("index")

    return render(request, "signup.html")
