from __future__ import unicode_literals

from django.db import models

# Create your models here.
class TimeStampeModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True