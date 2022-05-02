from django.shortcuts import render

from .models import Software
from .forms import PublishSoftwareForm

# Create your views here.
def publish_software_view(request, *args, **kwargs):
    publish_form = PublishSoftwareForm(request.POST or None)
    if publish_form.is_valid():
        pass
    else:
        print(publish_form.errors)

    context = {
        'form': publish_form,
    }
    
    return render(request, 'pages/publish_software.html', context)
