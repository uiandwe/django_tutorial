from django.shortcuts import render
from .decorators import decorator
from django.http import JsonResponse
import pika



@decorator
def message(request):
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        'localhost'))
    channel = connection.channel()

    return JsonResponse({'foo': 'bar'})

