from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='entry'),
	url(r'^home', views.home, name='home'),
	url(r'^bride', views.bride, name='bride'),
	url(r'^reception', views.reception, name='reception'),
	url(r'^ceremony', views.ceremony, name='ceremony'),
	url(r'^groom', views.groom, name='groom'),
]
