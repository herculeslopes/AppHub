from django.shortcuts import render

from .forms import UserLoginForm, UserSignupForm

# Create your views here.
def user_login_view(request, *args, **kwargs):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        print('data is valid')

    username = request.POST.get('username-input')
    password = request.POST.get('password-input')
    
    print(f'Usermane: {username}')
    print(f'Password: {password}')

    if username == 'Hércules' and password == 'senha':
        return render(request, "home.html", {})
    else:
        return render(request, "login.html", {})


def user_signup_view(request, *args, **kwargs):
    form = UserSignupForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }

    username = request.POST.get('username-input')
    password_1 = request.POST.get('password-input')
    password_2 = request.POST.get('password-confirmation-input')

    print(f'Username: {username}')
    print(f'Password: {password_1}')
    print(f'Password: {password_2}')

    return render(request, "signup.html", context)
