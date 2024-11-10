from django.shortcuts import render
from django.shortcuts import render
from .forms import UserRegister
from .models import *


def home(request):
    return render(request, 'home.html')


def shop(request):
    games = ['Atomic Heart', 'Cyberpunk 2077']
    return render(request, 'shop.html', {'games': games})


def about(request):
    return render(request, 'about.html')


def menu(request):
    return render(request, 'menu.html')


users = ['user1', 'user2', 'user3']


def sign_up_by_html(request):
    info = {}
    form = UserRegister()
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            else:
                if Buyer.objects.filter(name=username).exists():
                    info['error'] = 'Пользователь уже существует'
                else:

                    Buyer.objects.create(name=username, password=password, age=age)
                    return render(request, 'success.html', {'username': username})

            info['form'] = form
            return render(request, 'registration_page.html', info)


def shop(request):
    games = Game.objects.all()
    return render(request, 'shop.html', {'games': games})


def sign_up_by_django(request):
    return sign_up_by_html(request)
