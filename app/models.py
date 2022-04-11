from django.db import models
import os
from deepgram_app import settings


def wrapper(user, filename):
    file_upload_dir = os.path.join(settings.MEDIA_ROOT, '')
    if os.path.exists(file_upload_dir):
        import shutil
        shutil.rmtree(file_upload_dir)
    return os.path.join(file_upload_dir, filename)


def path_file():
    return wrapper


class Audio_store(models.Model):
    record = models.FileField(upload_to=path_file())

    class Meta:
        db_table = 'Audio_store'
