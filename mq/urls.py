from django.urls import path

from . import views

app_name = 'mq'
urlpatterns = [
    path('', views.message)
]