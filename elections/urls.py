from django.conf.urls import url
from . import views #.은 현재 폴더(elections)를 의미합니다.

urlpatterns = [
    url(r'^$', views.index), #위의 urls.py와는 달리 include가 없습니다.
    url(r'^areas/(?P<area>.+)/$', views.areas),
    url(r'^polls/(?P<poll_id>\d+)/$', views.polls), #이 url에 대한 요청을 views.polls가 처리하게 만듭니다.
]