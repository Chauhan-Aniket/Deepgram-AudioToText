from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import HomePageView, audio_upload
from django.views.generic.base import RedirectView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("form/", audio_upload, name="audio_upload"),
    path('favicon.png', RedirectView.as_view(
        url='favicon.png'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
