from django.urls import path

from . import views
from django.conf.urls import url

app_name = 'lotte'
urlpatterns = [
    url(r'', views.LotteList.as_view()),
]