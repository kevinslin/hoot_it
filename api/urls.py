from django.conf.urls.defaults import patterns, include, url

from piston.resource import Resource
from piston.authentication import HttpBasicAuthentication
from api.handlers import RatingHandler, TimerHandler


auth = HttpBasicAuthentication(realm = "Example Realm")
ad = { 'authentication':auth}

#foo_handler = Resource(FooHandler, authentication = auth)

#workout_resource = Resource(handler = WorkoutHandler)
#arbitrary_resource = Resource(handler=ArbitraryDataHandler, **ad)
rating_resource = Resource(handler = RatingHandler)
timer_resource = Resource(handler = TimerHandler)

urlpatterns = patterns('',
    url(r'^rating/', rating_resource, name="api_rating"),
    url(r'^time/', timer_resource, name="api_time"),
)
