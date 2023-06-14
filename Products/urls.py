from django.urls import path,include
from Products import views

urlpatterns = [
    path('admin/', views.Products),

]