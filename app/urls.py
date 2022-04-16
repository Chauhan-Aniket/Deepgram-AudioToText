from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib import admin
from .views import HomePageView, audio_upload

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", HomePageView.as_view(), name="home"),
    path("form/", audio_upload, name="audio_upload"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
