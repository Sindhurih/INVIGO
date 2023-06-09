from django.contrib import messages
from django.contrib.auth.hashers import check_password

from django.shortcuts import render, redirect

from main.models import User


def home(request):
    return render(request, 'home.html')


# Create your views here.
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


def addProduct(request):
    return render(request, 'addProduct.html')
