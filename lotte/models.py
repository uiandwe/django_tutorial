from django.db import models


class Lotte(models.Model):
    lottery_date = models.DateField()
    nubmer1 = models.IntegerField()
    nubmer2 = models.IntegerField()
    nubmer3 = models.IntegerField()
    nubmer4 = models.IntegerField()
    nubmer5 = models.IntegerField()
    nubmer6 = models.IntegerField()
    bonus = models.IntegerField()
