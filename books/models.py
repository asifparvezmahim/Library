from django.db import models
from categories.models import Category


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    discription = models.TextField()
    price = models.CharField(max_length=6)
    category = models.ManyToManyField(Category)
    image = models.ImageField(upload_to="books/media/uploads/", blank=True, null=True)

    def __str__(self):
        return self.title
