from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import HomePageView, Audio_upload

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("form/", Audio_upload, name="audio_upload"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
