from django.shortcuts import render
from django.http.response import HttpResponse


def blog_page(request):
    return HttpResponse('Hello!!!')
