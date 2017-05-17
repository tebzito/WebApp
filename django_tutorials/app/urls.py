"""
Definition of urls for MusicStore.
"""

from datetime import datetime
from django.conf.urls import url, patterns
from django.contrib import admin
from app.forms import BootstrapAuthenticationForm 
#from app import views as app_views
#from django.contrib.auth import views as auth_views
#from app.views import artists, contact, artistdetails, about
#from django.contrib.auth.views import login, logout
admin.autodiscover()

#urlpatterns = [url(r'^admin/', admin.site.urls),
#	       ]


urlpatterns = patterns('',
	url(r'^artists$', 'app.views.artists', name='artists'),
	#url(r'^artists/(?P<name>[A-Za-z]+)$', 'app.views.artistdetails', name='artistdetails'),
	url(r'^artists/create$', 'app.views.artistcreate', name='artistcreate'),
	url(r'^artists/(?P<id>\d+)$', 'app.views.artistdetails', name='artistdetails'),
	url(r'^$', 'app.views.home', name='home'),
	url(r'^contact$','app.views.contact', name='contact'),
	url(r'^about', 'app.views.about', name='about'),
	#url(r'^seed', 'app.views.seed', name='seed'),
	url(r'^login/$',
	    'django.contrib.auth.views.login',
	    {
		'template_name': 'app/login.html',
		'authentication_form': BootstrapAuthenticationForm,
		'extra_context':
		{
		    'title': 'Log in',
		    'year': datetime.now().year,
		}    
		
	    },
	    name='login'),
	url(r'^logout$',
	    'django.contrib.auth.views.logout',
	    {
	      'next_page': '/',
	    },
	    name='logout'),
	)
