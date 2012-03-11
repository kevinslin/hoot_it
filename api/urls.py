from django.conf.urls.defaults import patterns, include, url

from piston.resource import Resource
from piston.authentication import HttpBasicAuthentication
from api.handlers import WorkoutHandler


auth = HttpBasicAuthentication(realm = "Example Realm")
ad = { 'authentication':auth}

#foo_handler = Resource(FooHandler, authentication = auth)

workout_resource = Resource(handler = WorkoutHandler)
#arbitrary_resource = Resource(handler=ArbitraryDataHandler, **ad)

urlpatterns = patterns('',
    url(r'^workout/(?P<username>[\w\d]+)/', workout_resource, name="api_workout"),
)
