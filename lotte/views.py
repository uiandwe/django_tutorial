from django.shortcuts import render
from rest_framework import generics
from .models import Lotte
from .serializers import LotteSerializer


class LotteList(generics.ListCreateAPIView):
    queryset = Lotte.objects.all()
    serializer_class = LotteSerializer
