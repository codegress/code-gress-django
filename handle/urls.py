from django.conf.urls import include, url
from . import views
urlpatterns = [
	url(r'^$',views.index,name='index'),
	url(r'^signup$',views.signup,name='signup'),
	url(r'^login$',views.login,name='login'),
	url(r'^login/recover$',views.recover,name='recover'),
	url(r'^logout$',views.logout,name='logout'),
	url(r'^challenges$',views.challenges,name='challenges'),
	url(r'^competitions$',views.competitions,name='competitions'),
	url(r'^updates$',views.updates,name='updates'),
	url(r'^messages$',views.messages,name='messages'),
	url(r'^recent$',views.recent,name='recent'),
	url(r'^search$',views.search,name='search'),
	url(r'settings/(?P<selected>[a-z]+)?$',views.profile,name='profile'),
	url(r'^(?P<handle>[a-z]+)/$',views.leaderboard,name='leaderboard'),
]