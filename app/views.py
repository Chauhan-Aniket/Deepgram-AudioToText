# Create your views here.
from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse
from .forms import AudioForm


class HomePageView(TemplateView):
    template_name = "home.html"


def Audio_store(request):
    if request.method == 'POST':
        form = AudioForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            return render(request, 'home.html')
    else:
        form = AudioForm()
    return render(request, 'audio.html', {'form': form})
