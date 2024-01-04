"""
URL configuration for mamar_bank project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core.views import HomeView
from books.views import home
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    # path("profile/", views.profile, name="profile"),
    path("category/<slug:category_slug>/", home, name="category_wise_post"),
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("transactions/", include("transactions.urls")),
    path("books/", include("books.urls")),
    path("categories/", include("categories.urls")),
    path("home/", include("core.urls")),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
