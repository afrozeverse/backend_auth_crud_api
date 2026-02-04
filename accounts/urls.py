from django.urls import path
from .views import Registerview,Loginview

urlpatterns = [
    path('register/', Registerview.as_view(),name='apiAuthRegister'),
    path('login/', Loginview.as_view(),name='apiAuthLogin'),
]