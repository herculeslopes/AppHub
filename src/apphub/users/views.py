from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from .forms import UserLoginForm, UserSignupForm


def user_login_view(request, *args, **kwargs):
    login_form = UserLoginForm(request.POST or None)
    if login_form.is_valid():
        username = login_form.cleaned_data['username']
        password = login_form.cleaned_data['password']

        user = authenticate(username=username, password=password)

        if user:
            django_login(request, user)
            return redirect('pages_home')
            # return HttpResponse('autenticado')
        
        else:
            return HttpResponse('email ou senha inválidos')

    context = {
        'form': login_form,
        'user': None,
    }

    return render(request, 'users/user_login.html', context)


def user_signup_view(request, *args, **kwargs):
    signup_form = UserSignupForm(request.POST or None)

    if signup_form.is_valid():
        signup_data = {
            'username': signup_form.cleaned_data['username'],
            'email': signup_form.cleaned_data['email'],
            'password': signup_form.cleaned_data['password'],
        }
        
        user = User.objects.filter(username=signup_data['username']).first()

        if user:
            return HttpResponse('Usuário já  existe')
        
        user = User.objects.create_user(
            username = signup_data['username'],
            email = signup_data['email'],
            password = signup_data['password'],
        )
        user.save()

        return redirect('pages_home')

    context = {
        'form': signup_form,
        'user': None,
    }

    return render(request, 'users/user_signup.html', context)


def user_logout_view(request, *args, **kwargs):
    django_logout(request)

    return redirect('pages_home')