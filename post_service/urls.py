from django.urls import path

from . import views
from django.conf.urls import url

from post_service.views import post_list


app_name = 'post'
urlpatterns = [
    url(r'^$', post_list)
    # path('', views.IndexView.as_view(), name='index'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]