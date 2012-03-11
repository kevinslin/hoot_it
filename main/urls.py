from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('main.views',
    url(r'^$', 'landing_page'),
    url(r'^index', 'index'),
    url(r'^example$', 'example'),
    
    url(r'^pset', 'pset'),
)
