from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from main.models import FoodCategory, Food, FoodComment


def index_view(request: HttpRequest):

    categories = FoodCategory.objects.all()

    context = {
        "categories": categories
    }

    return render(request, "index.html", context=context)


def category_detail(request: HttpRequest, pk):
    category = get_object_or_404(FoodCategory, pk=pk)
    foods = Food.objects.filter(category=category, is_active=True).order_by("-created_at")
    context = {
        "category": category,
        "foods": foods
    }

    return render(request, "category-detail.html", context=context)
    


def food_detail(request: HttpRequest, pk):
    food = get_object_or_404(Food, pk=pk)

    if request.method == "POST":
        body = request.POST.get("body")

        comment = FoodComment.objects.create(
            food=food,
            user=request.user,
            body=body
        )
        return redirect("food_detail", pk=food.id)

    context = {
        "food": food
    }
    return render(request, "food-detail.html", context)



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
