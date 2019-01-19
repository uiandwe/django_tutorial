from django.shortcuts import render
from rest_framework import generics
from .models import Lotte
from .serializers import LotteSerializer
import random

class LotteList(generics.ListCreateAPIView):
    queryset = Lotte.objects.all()
    serializer_class = LotteSerializer


class LotteNumber(generics.ListAPIView):
    queryset = Lotte.objects.all()
    # number_array = [[x, 0] for x in range(46)]
    # values = ["number1", "number2", "number3", "number4", "number5", "number6"]
    # for lotteObj in list(queryset):
    #     for i in range(6):
    #         lotteNum = getattr(lotteObj, values[i])
    #         number_array[lotteNum][1] += 1
    # number_array = sorted(number_array, key=lambda l:l[1], reverse=True)
    #
    # numbers = [x for x in range(1, 47)]
    # random.shuffle(numbers)
    # dict = {}
    # index = 1
    # queryset = Lotte.objects.all()
    # print(numbers[0:6])
    serializer_class = LotteSerializer