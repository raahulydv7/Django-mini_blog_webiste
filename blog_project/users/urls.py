from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.user_register_view, name="register"),
    path("login/", views.User_login_view, name="login"),
    path("profile/", views.User_profile_view, name="profile"),
    path("logout/", views.user_logout_view, name="logout"),
]
