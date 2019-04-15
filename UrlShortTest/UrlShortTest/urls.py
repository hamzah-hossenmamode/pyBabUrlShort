from django.urls import path,re_path
from app import views


urlpatterns = [
    path('', views.error,name='error'),
    path('shorten_url', views.shorten_url,name='shorten_url'),
    re_path('^.{8}/$', views.shorts,name='shorts'),
    re_path('^.*/$', views.error,name='error'),
]
