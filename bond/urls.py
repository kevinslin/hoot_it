from django.conf.urls.defaults import *

urlpatterns = patterns('bond.views',
    url(r'^$', 'index'),
)
