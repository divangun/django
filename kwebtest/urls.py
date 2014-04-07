from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'textpro.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

	url(r'^me/([\w]+)/([\w]+)/([\w]+)/', 'kwebtest.views.me'),	
	url(r'^$', 'kwebtest.views.htmltest'),
	url(r'^([\w]+)/', 'kwebtest.views.hello'),
)
