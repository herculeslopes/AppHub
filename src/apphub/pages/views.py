from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from softwares.models import Software
# Create your views here.
# def home_view(request, *args, **kwargs):
#     # return HttpResponse("<h1>Hello World</h1>")
#     if cache.get('user') != None:

#         box_list = [x for x in range(10)]
#         return render(request, "home.html", {'box_list': box_list})

#     return redirect('user_login')


@login_required(login_url='/auth/login/')
def home_page_view(request, *args, **kwargs):
    if request.method == 'GET':
        all_softwares = Software.objects.all()

        context = {
            'softwares': all_softwares
        }

        print('not searched')

    else:
        searched = request.POST['search-input']
        softwares = Software.objects.filter(name__contains=searched)

        context = {
            'searched': searched,
            'softwares': softwares,
        }

        print('searched')


    return render(request, 'pages/home.html', context)
    

def test_page_view(request, *args, **kwargs):
    return render(request, 'test.html', {})
    