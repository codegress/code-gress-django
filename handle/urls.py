from django.conf.urls import include, url
from . import views
urlpatterns = [
	url(r'^$',views.index,name='index'),
	url(r'^signup$',views.signup,name='signup'),
	url(r'^login$',views.login,name='login'),
	url(r'^login/recover$',views.recover,name='recover'),
	url(r'^logout/$',views.logout,name='logout'),
	url(r'^(?P<handle>[a-z]+)/$',views.leader,name='leader'),
]