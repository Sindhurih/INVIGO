from django.urls import path, include
from Products import views

urlpatterns = [
    path('/', views.AddPurchase),
]
