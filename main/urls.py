from django.urls import path, include
from main import views

urlpatterns = [
    path('', views.login),
    path('home/', views.home),
    path('', include('Products.urls')),
    path('', include('Purchase')),
]
