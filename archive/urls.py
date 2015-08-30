from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^series/(?P<pk>[0-9]+)/$', views.series, name='series'),
]
