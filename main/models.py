from django.db import models
from django.contrib.auth.models import User
import datetime

from userena.models import UserenaBaseProfile

class Question(models.Model):
    def __unicode__(self):
        return self.name
    name = models.CharField(max_length=100)
    details = models.TextField()

class ProblemSet(models.Model):
    """
    A problem set
    """
    def __unicode__(self):
        return self.name
    name = models.CharField(max_length=100)
    question = models.ForeignKey(Question)

class Course(models.Model):
    """
    A course
    """
    def __unicode__(self):
        return self.name

    name = models.CharField(max_length=100)
    course_id = models.IntegerField()
    problem_set = models.ForeignKey(ProblemSet)

class UserProfile(UserenaBaseProfile):
    user = models.OneToOneField(User, unique=True)
    course = models.ForeignKey(Course, null = True, blank = False)

class QuestionStats(models.Model):
    rating = models.IntegerField()
    start_time = models.DateTimeField()
    stop_time = models.DateTimeField()
    question = models.ForeignKey(Question)
    profile = models.ForeignKey(UserProfile)









