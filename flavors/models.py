from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.
from core.models import TimeStampeModel

class Flavor(TimeStampeModel):
    title = models.CharField(max_length=200)


class PublishedManager(models.Manager):
    use_for_related_fields = True

    def published(self, **kwargs):
        return self.filter(pub_date__lte=timezone.now(), **kwargs)

class FlavorReview(models.Model):
    review = models.CharField(max_length=255)
    pub_date = models.DateTimeField()

    objects = PublishedManager()