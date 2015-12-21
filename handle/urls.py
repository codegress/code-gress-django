from django.conf.urls import include, url
from . import views
urlpatterns = [
	url(r'^$',views.index,name='index'),
	url(r'^signup$',views.signup,name='signup'),
	url(r'^login$',views.login,name='login'),
	url(r'^login/recover$',views.recover,name='recover'),
	url(r'^logout/$',views.logout,name='logout'),
	url(r'^challenges/$',views.challenges,name='challenges'),
	url(r'^competitions/$',views.competitions,name='competitions'),
	url(r'^(?P<handle>[a-z]+)/caf$',views.caf,name='caf'),
	url(r'^(?P<handle>[a-z]+)/settings/(?P<selected>[a-z]+)?$',views.profile,name='profile'),
	url(r'^(?P<handle>[a-z]+)/challenges$',views.recent_challenges,name='recent_challenges'),
	url(r'^(?P<handle>[a-z]+)/updates$',views.updates,name='updates'),
	url(r'^(?P<handle>[a-z]+)/feeds$',views.feeds,name='feeds'),
	url(r'^(?P<handle>[a-z]+)/$',views.codegress,name='codegress'),
]