from __future__ import unicode_literals

from django.db import models

# Create your models here.
class TimeStampeModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class FileModel(models.Model):
    folder = models.CharField(max_length=255)
    dateFolderPath = models.CharField(max_length=255)
    fileName = models.CharField(max_length=255)

    class Meta:
        abstract = True