from django.urls import path

from . import views

app_name = 'score'
urlpatterns = [
    path('', views.score, name='score')
]