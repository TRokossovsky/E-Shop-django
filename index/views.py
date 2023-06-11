from django.shortcuts import render
from .forms import UserRegistrationForm
from .models import Product


def index(request):
    products = Product.objects.all()
    return render(request, 'index/index.html', {'products': products})


def catalogue(request):
    return render(request, 'index/catalogue.html')


def about(request):
    return render(request, 'index/about.html')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'index/login.html')
    else:
        form = UserRegistrationForm()
    return render(request, 'index/register.html', {'form': form})


def login(request):
    return render(request, 'index/login.html')
