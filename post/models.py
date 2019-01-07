from django.db import models
from core.models import TimeStampeModel


class Post(TimeStampeModel):
    title = models.CharField(max_length=255)
    content = models.TextField()




