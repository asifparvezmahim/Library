from django.shortcuts import render
from .models import Book
from categories.models import Category


# Create your views here.
def home(request, category_slug=None):
    data = Book.objects.all()
    if category_slug is not None:
        category = Category.objects.get(slug=category_slug)
        data = Book.objects.filter(category=category)
    category = Category.objects.all()
    return render(request, "show_books.html", {"data": data, "category": category})
