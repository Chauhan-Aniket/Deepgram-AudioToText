# Create your views here.
from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse
from .forms import AudioForm
from django.core.files.storage import FileSystemStorage


class HomePageView(TemplateView):
    template_name = "home.html"


def Audio_upload(request):
    if request.method == 'POST':
        form = AudioForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            myfile = request.FILES['record']
            fs = FileSystemStorage()
            uploaded_file_url = fs.url(myfile)
            print(uploaded_file_url)
            return render(request, 'audio.html', {
                'uploaded_file_url': uploaded_file_url
            })
    else:
        form = AudioForm()
    return render(request, 'form.html', {'form': form})
