from django.shortcuts import render
from rest_framework import generics
from .models import Lotte
from .serializers import LotteSerializer


class LotteList(generics.ListCreateAPIView):
    queryset = Lotte.objects.all()
    serializer_class = LotteSerializer


class LotteNumber(generics.ListAPIView):
    queryset = Lotte.objects.all()
    print("--------")
    print(queryset)
    dict = {}
    values = ["number1", "number2", "number3", "number4", "number5", "number6"]
    for lotteObj in list(queryset):
        print(dir(lotteObj))
        print(lotteObj["nubmer4"])

        # for i in range(6):
        #     lotteNum = lotteObj[values[i]]
        #     if lotteNum in dict:
        #         dict[lotteNum] += 1
        #     else:
        #         dict[lotteNum] = 1

    print(dict)
    serializer_class = LotteSerializer