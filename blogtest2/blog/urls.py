from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^index0/$', views.index0),
    url(r'^$', views.index),
    url(r'^index/$', views.index),
]
