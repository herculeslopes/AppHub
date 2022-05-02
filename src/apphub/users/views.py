from django.shortcuts import render, redirect
from django.core.cache import cache

from .models import User
from .forms import UserLoginForm, UserSignupForm


# Create your views here.
# def user_login_view(request, *args, **kwargs):
#     form = UserLoginForm(request.POST or None)
#     if form.is_valid():
#         print('data is valid')

#     username = request.POST.get('username-input')
#     password = request.POST.get('password-input')
    
#     print(f'Usermane: {username}')
#     print(f'Password: {password}')

#     if username == 'Hércules' and password == 'senha':
#         return render(request, "home.html", {})
#     else:
#         return render(request, "login.html", {})


# def user_signup_view(request, *args, **kwargs):
#     signup_form = UserSignupForm()
#     if request.method == 'POST':
#         signup_form = UserSignupForm(request.POST or None)
#         if signup_form.is_valid():
            
#             # Server validation of the data
#             if validate_user_signup(signup_form.cleaned_data):
#                 signup_data = {
#                     'username': signup_form.cleaned_data['username'],
#                     'password': signup_form.cleaned_data['password'],
#                 }
#                 User.objects.create(**signup_data)
#         else:
#             print(signup_form.errors)

#     context = {
#         'form': signup_form
#     }

#     return render(request, "signup.html", context)


def user_login_view(request, *args, **kwargs):
    login_form = UserLoginForm(request.POST or None)
    if login_form.is_valid():
        print('data is valid')

        username = login_form.cleaned_data['username']
        password = login_form.cleaned_data['password']

        queryset = None
        try:
            queryset =  User.objects.get(username__exact=username, password__exact=password)
        except Exception:
            print('ero')
            print(Exception)

        if queryset != None:

            cache.set('user', queryset)

            # request.session['user'] = queryset

            print(queryset)
            print(type(queryset))
            
            context = {
            'user': queryset
            }

            # return render(request, "home.html", context)
            return redirect('pages_home')
            
        


    else:
        print(login_form.errors)
        print('data is not valid')
    # if username == 'Hércules' and password == 'senha':
    #     return render(request, "home.html", {})
    # else:

    context = {
        'form': login_form,
        'user': None,
    }

    return render(request, "users/user_login.html", context)


def user_signup_view(request, *args, **kwargs):
    signup_form = UserSignupForm(request.POST or None)
    
    if signup_form.is_valid():
        signup_data = {
            'username': signup_form.cleaned_data['username'],
            'email': signup_form.cleaned_data['email'],
            'password': signup_form.cleaned_data['password'],
        }
        
        current_user = User.objects.create(**signup_data)
        cache.set('user', current_user)

        message = 'Signup Completed'

        return redirect('pages_home')

    else:
        message = 'Error on Signup'
        print(signup_form.errors)

    context = {
        'form': signup_form,
        'message': message,
        'user': None,
    }

    return render(request, "users/user_signup.html", context)


def user_logout_view(request, *args, **kwargs):
    cache.delete('user')
    return redirect('user_login')