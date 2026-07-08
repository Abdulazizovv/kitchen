from django.urls import path
from main.views import (
    index_view, 
    login_view, 
    logout_view, 
    signup_view,

    category_detail,
    )


urlpatterns = [
    path("", index_view, name="index"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("signup/", signup_view, name="signup"),

    path("category/<int:pk>/", category_detail, name="category_detail")
]