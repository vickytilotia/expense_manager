from django.urls import path
from .views import RegistrationView
from . import views

urlpatterns = [
    path('register', RegistrationView.as_view(), name ="register"),
    
]
