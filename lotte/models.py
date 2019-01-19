from django.db import models


class Lotte(models.Model):
    lottery_date = models.DateField()
    number1 = models.IntegerField()
    number2 = models.IntegerField()
    number3 = models.IntegerField()
    number4 = models.IntegerField()
    number5 = models.IntegerField()
    number6 = models.IntegerField()
    bonus = models.IntegerField()
