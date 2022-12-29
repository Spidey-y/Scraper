from django.urls import path
from .views import RegisterUserView, LoginView, LogoutView, ProfileView


urlpatterns = [
    path('register', RegisterUserView.as_view(), name="Register"),
    path('login', LoginView.as_view(), name="Login"),
    path('logout', LogoutView, name="Logout"),
    path('profile', ProfileView, name="Profile")
]
