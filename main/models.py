from django.db import models
from django.contrib.auth.models import User
import datetime

CHOICES_GENDER = (
    (1, 'Male'),
    (2, 'Female'),
)

class UserProfile(models.Model):
    """
    User Profile. User can be an athlete or a coach.
    """
    def __unicode__(self):
        return self.user.username

    user = models.OneToOneField(User)
    gender = models.PositiveSmallIntegerField('gender',
            choices=CHOICES_GENDER, blank=True,
            null = True)
    birthday = models.DateField(
            default=datetime.datetime.utcfromtimestamp(83850))
    pic = models.ImageField(upload_to='img/profile', blank=True)


    @property
    def age(self):
        today = datetime.date.today()
        if self.birthday:
            #FIXME: hack, not accurate
            return "%s" % str(
                    (today - self.birthday).days / 365
                    )

