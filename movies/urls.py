from django.urls import path

from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.question, name='question'),
    path('ranking/', views.ranking, name='ranking')
]