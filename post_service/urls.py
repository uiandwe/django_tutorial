from django.urls import path

from . import views
from django.conf.urls import url

from post_service.views import post_list

app_name = 'post'
urlpatterns = [
    url(r'^$', post_list)
]