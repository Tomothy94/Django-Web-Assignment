from django.conf.urls import include, url
from . import views

app_name = 'teams'
urlpatterns = [
    # /teams/
    url(r'^$', views.index, name='index'),


    # /teams/1/
    url(r'^(?P<id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<id>[0-9]+)/player_create$', views.player_create, name='player_create'),

]

