from django.contrib import messages

from django.shortcuts import render, redirect


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




