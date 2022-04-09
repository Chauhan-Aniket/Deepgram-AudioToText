from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import HomePageView, Audio_store

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("audio/", Audio_store)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
