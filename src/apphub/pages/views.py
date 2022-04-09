from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.core.cache import cache

# Create your views here.
def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello World</h1>")
    if cache.get('user') != None:

        box_list = [x for x in range(10)]
        return render(request, "home.html", {'box_list': box_list})

    return redirect('user_login')
