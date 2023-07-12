from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from .models import Product


def index(request):

    return render(request, 'index/index.html')


def catalogue(request):
    products = Product.objects.all()
    return render(request, 'index/catalogue.html', {'products': products})


def about(request):
    return render(request, 'index/about.html')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'index/catalogue.html')
    else:
        form = UserRegistrationForm()
    return render(request, 'index/register.html', {'form': form})


def login(request):
    return render(request, 'index/login.html')
