from django.conf.urls import include, url
from . import views
urlpatterns = [
	url(r'^$',views.index,name='index'),
	url(r'^signup$',views.signup,name='signup'),
	url(r'^signup/check/handle$',views.check_handle,name='check handle'),
	url(r'^signup/check/email$',views.check_email,name='check email'),
	url(r'^signup/check/pass$',views.check_pass,name='check password'),
	url(r'^signin$',views.login,name='login'),
	url(r'^recover$',views.recover,name='recover'),
	url(r'^logout$',views.logout,name='logout'),
	url(r'^challenges$',views.challenges,name='challenges'),
	url(r'^competitions$',views.competitions,name='competitions'),
	url(r'^updates$',views.updates,name='updates'),
	url(r'^messages$',views.messages,name='messages'),
	url(r'^recent$',views.recent,name='recent'),
	url(r'^search$',views.search,name='search'),
	url(r'settings/(?P<selected>[a-z]+)?$',views.profile,name='profile'),
	url(r'^(?P<handle>[a-z]+)$',views.leaderboard,name='leaderboard'),
	url(r'^(?P<handle>[a-z]+)/follow$',views.follow,name='follow'),
]