from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views
from django.conf.urls import include
from django.urls import path


urlpatterns = [
    url(r'', views.SnippetList.as_view()),
    url(r'<int:pk>/', views.SnippetDetail.as_view()),
    # url('', views.SnippetList.as_view()),
    # url('<int:pk>/', views.SnippetDetail.as_view()),
    # url(r'^api-auth/', include('rest_framework.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)