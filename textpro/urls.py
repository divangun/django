from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'textpro.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^kweb/',  include('kwebtest.urls')),
	url(r'^parse/', include('parse.urls')),
	url(r'^$', 'kwebtest.views.main'),
)
