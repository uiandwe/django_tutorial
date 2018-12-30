from django.db import models

from core.models import FileModel

class Movies(FileModel):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)