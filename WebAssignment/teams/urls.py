from django.conf.urls import include, url
from . import views

urlpatterns = [
    # /teams/
    url(r'^$', views.index, name='index'),


    # /teams/1/
    url(r'^(?P<team_ID>[0-9]+)/$', views.detail, name='detail'),
]

