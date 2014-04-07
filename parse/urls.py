from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'textpro.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

	url(r'^soup/([\w]+)/([\w]+)/([\w]+)/', 'parse.views.me'),	
	url(r'^soup/([\w]*)', 'parse.views.soupView'),
	url(r'^soup', 'parse.views.soupView'),
	
	url(r'^keyword/([\w]+)/([\w]*)', 'parse.views.soupkeywordView'),
	url(r'^keyword/([\w]+)', 'parse.views.soupkeywordView'),

	url(r'^google/([\w]+)/([\w]*)', 'parse.views.soupgoogleView'),
	url(r'^google/([\w]+)', 'parse.views.soupgoogleView'),

	url(r'^me/([\w]+)/([\w]+)/([\w]+)/', 'parse.views.me'),	
	url(r'^([\w]+)/', 'parse.views.hello'),
)
