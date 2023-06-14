from django.urls import path, include
from django.contrib.auth import views as auth_views
from main import views

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('home/', views.home, name='home'),
    # product urls
    path('products/add/', views.addProduct, name='addProduct'),
    path('products/list/', views.list_product, name='list_product'),

    # purchase order urls
    path('purchase/add/', views.add_purchase, name='add_purchase')
]
