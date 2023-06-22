from django.contrib import messages
from django.contrib.auth.models import User

from django.shortcuts import render, redirect
from main.models import User


def login(request):
    if request.method == "POST":
        username = request.POST.get('email')
        pas = request.POST.get('password')
        res = User.objects.filter(email_id=username, password=pas)
        if len(res) > 0:
            request.session['email'] = res[0].email_id
            return redirect('/home/')
        else:

            messages.error(request, "*Invalid Credentials*")
            return render(request, "Login.html")

    else:
        return render(request, 'login.html')



def home(request):
    return render(request, 'home.html')


# Product views
def addProduct(request):
    print(request.method)
    if request.method == 'GET':
        return render(request, 'addProduct.html')
    elif request.method == 'POST':
        # get form data and process.
        return redirect('/products/list/')


def list_product(request):
    return render(request, 'listProduct.html')


# Purchase views
def add_purchase(request):
    if request.method == 'GET':
        return render(request, 'AddPurchase.html')
    elif request.method == 'POST':
        # get form data and process.
        return redirect('/purchase/list/')
