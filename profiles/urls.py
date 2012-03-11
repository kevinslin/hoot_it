from django.conf.urls.defaults import patterns, include, url
from django.forms import ModelForm

from main.models import UserProfile

class profile_form(ModelForm):
    class Meta:
        model = UserProfile
        exclude = ("user")

urlpatterns = patterns('',
    url(r'^edit/$',
        view = 'simpleapps.profiles.views.profile_edit',
        name = 'profile_edit',
        kwargs = {
            'form_class': profile_form,
        }
    ),
    url(r'^(?P<username>[-\w]+)/$',
        view = 'simpleapps.profiles.views.profile_detail',
        name = 'profile_detail'
    ),
    url (r'^$',
        view = 'simpleapps.profiles.views.profile_list',
        name = 'profile_list',
    ),
)
