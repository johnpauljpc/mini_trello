from django.urls import path
from .views import UserRegistrationView, LoginView, ProfileView


urlpatterns = [
    path("register/", UserRegistrationView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path('profile/', ProfileView.as_view(), name='user-profile'),
    
]