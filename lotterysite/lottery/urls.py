from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^post/$', views.post, name='post'),
	url(r'^registerConfirmed/$', views.registerConfirmed, name='registerConfirmed'),
	]