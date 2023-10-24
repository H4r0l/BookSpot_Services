from django.urls import path
from .views import authAPI

urlpatterns = [
    path('', authAPI.as_view())
]