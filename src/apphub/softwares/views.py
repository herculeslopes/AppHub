from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Software
from .forms import PublishSoftwareForm

# Create your views here.
@login_required(login_url='/auth/login/')
def publish_software_view(request, *args, **kwargs):
    user = request.user

    publish_form = PublishSoftwareForm(request.POST or None)
    if publish_form.is_valid():
        publish_data = {
            'publisher': user,
            'name': publish_form.cleaned_data['name'],
            'version': publish_form.cleaned_data['version'],
            'description': publish_form.cleaned_data['description'],
            'project_url': publish_form.cleaned_data['project_url'],
        }

        supported_platforms = publish_form.cleaned_data['platforms']
        published_software = Software.objects.create(**publish_data)
        published_software.platforms.set(supported_platforms)

        return redirect('pages_home')
        
    else:
        print('Error on Publishing Software')
        print(publish_form.errors)

    context = {
        'form': publish_form,
    }
    
    return render(request, 'pages/publish_software.html', context)


def software_page_view(request, *args, **kwargs):
    id = request.GET['id']
    # return HttpResponse(f'Resquest: {request.GET["id"]}')

    software = Software.objects.get(software_id=id)

    context = {
        'software': software,
    }

    return render(request, 'pages/software_page.html', context)


def software_search_view(request, *args, **Kwargs):
    pass