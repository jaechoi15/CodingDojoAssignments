from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^home$', views.home),
    url(r'^add$', views.add),
    url(r'^insert$', views.insert_book),
    url(r'^book/(?P<book_id>\d+)$', views.book),
    url(r'^users/(?P<user_id>\d+)$', views.user),
    url(r'^books/(?P<book_id>\d+)/add_review$', views.add_review),
    url(r'^books/(?P<book_id>\d+)/delete/(?P<review_id>\d+)$', views.delete),
    url(r'^logout$', views.logout)
]