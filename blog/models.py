from __future__ import unicode_literals

from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    reg_date = models.DateTimeField(auto_created=True, auto_now=True)
