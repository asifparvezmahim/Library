from django.urls import path, include
from .views import pageHome

urlpatterns = [
    path("homepage/", pageHome, name="pageHome"),
]
