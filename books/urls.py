from django.urls import path
from books import views

urlpatterns = [
    path("show_book", views.home, name="homepage"),
]
