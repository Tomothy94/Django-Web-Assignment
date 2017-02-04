from django.conf.urls import include, url
from . import controllers

app_name = 'teams'
urlpatterns = [
    # /teams/
    url(r'^$', controllers.index, name='index'),


    # /teams/1/
    url(r'^(?P<id>[0-9]+)/$', controllers.detail, name='detail'),
    url(r'^(?P<id>[0-9]+)/player_create$', controllers.player_create, name='player_create'),
    url(r'^(?P<id>[0-9]+)/player_edit/(?P<playerid>[0-9]+)$', controllers.player_edit, name='player_edit'),
    url(r'^(?P<id>[0-9]+)/player_delete/(?P<playerid>[0-9]+)$', controllers.player_delete, name='player_delete'),
]