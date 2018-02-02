from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^main$', views.main),
    url(r'^login$', views.login),
    url(r'^travels$', views.travels),
    url(r'^travels/add$', views.add),
]