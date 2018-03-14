from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^amadon$', views.main),
    url(r'^amadon/buy$', views.process),
    url(r'^amadon/checkout$', views.checkout),
    url(r'^clear$', views.clear)
]