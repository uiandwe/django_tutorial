"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import include
# from rest_framework_swagger.views import  get_swagger_view
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token
from django.urls import path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from blog.views import blog_page, blog_api
from quickstart.views import UserViewSet, GroupViewSet
from article.views import ArticleViewSet
import member.api

# schema_view = get_swagger_view(title='rest API')

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   validators=['flex', 'ssv'],
   public=True,
   # permission_classes=(permissions.AllowAny,),
)


router = routers.DefaultRouter()
router.register(r'member', member.api.MemberViewSet)
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
# router.register(r'article', ArticleViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # path('', TemplateView.as_view(template_name="../templates/index.html")),
    url(r'api/auth/', include('djoser.urls.authtoken')),
    url(r'^polls/', include('polls.urls')),
    url(r'^movies/', include('movies.urls')),
    url(r'^score/', include('score.urls')),
    url(r'^journal/', include('journal.urls')),
    url(r'^rest-api/', include('rest_framework.urls')),
    url(r'^rest-swagger/', schema_view),

    url(r'^blog/', blog_page),
    url(r'api/blog/', blog_api.as_view()),
    url(r'user/', include('user_manager.urls')),
    url(r'board/', include('post_service.urls')),
    url(r'^api/', include(router.urls)),
    url(r'api/member/', include((router.urls, 'member'), namespace='api')),
    url(r'api/post/', include('post.urls')),
    url(r'api/article/', include('article.urls')),
    url(r'api/todo/', include('todos.urls')),
    url(r'api/snippets/', include('snippets.urls')),
    # url(r'api/userSnippets/', include('snippets.userUrls')),
    # url(r'^api/doc', get_swagger_view(title='Rest API Document')),
    url(r'^api/doc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    url(r'api/api-token-auth/', obtain_jwt_token),
    url(r'api/api-token-verify/', verify_jwt_token),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'article', TemplateView.as_view(template_name='index.html'))

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
