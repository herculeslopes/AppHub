from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello World</h1>")
    box_list = [x for x in range(10)]
    return render(request, "home.html", {'box_list': box_list})
