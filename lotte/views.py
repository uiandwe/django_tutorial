from django.shortcuts import render
from rest_framework import generics
from .models import Lotte
from .serializers import LotteSerializer
import random
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view


class LotteList(generics.ListCreateAPIView):
    queryset = Lotte.objects.all()
    serializer_class = LotteSerializer


@api_view()
def LotteNumber(request):
    # queryset = Lotte.objects.all()
    # number_array = [[x, 0] for x in range(46)]
    # values = ["number1", "number2", "number3", "number4", "number5", "number6"]
    # for lotteObj in list(queryset):
    #     for i in range(6):
    #         lotteNum = getattr(lotteObj, values[i])
    #         number_array[lotteNum][1] += 1
    # number_array = sorted(number_array, key=lambda l:l[1], reverse=True)

    dict = {}
    index = 1
    while index <= 5:
        numbers = [x for x in range(1, 47)]
        random.shuffle(numbers)
        number_set_filter = sorted(numbers[0:6])
        number_set_filter = ','.join(str(e) for e in number_set_filter)
        number_set_count = Lotte.objects.filter(number_set=number_set_filter).count()
        if number_set_count == 0:
            dict[index] = number_set_filter
            index += 1

    return Response(dict)

