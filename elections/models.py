from django.db import models


class Candidate(models.Model):
    name = models.CharField(max_length=10)
    introduction = models.TextField()
    area = models.CharField(max_length=15)
    party_number = models.IntegerField(default=1)

    def __str__(self):
        return self.name  # object를 출력하면 name이 보입니다.