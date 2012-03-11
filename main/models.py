from django.db import models
from django.contrib.auth.models import User
import datetime

from userena.models import UserenaBaseProfile

class Course(models.Model):
    """
    A course
    """
    def __unicode__(self):
        return self.name

    name = models.CharField(max_length=100)
    course_id = models.IntegerField()


class ProblemSet(models.Model):
    """
    A problem set
    """
    def __unicode__(self):
        return self.name
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, blank=True, null=True)
    due_date = models.DateTimeField()

    def current():
        """
        If due date is in future
        """
        today = datetime.datetime.today()
        return self.due_date > today


class Question(models.Model):
    def __unicode__(self):
        return self.name
    name = models.CharField(max_length=100)
    details = models.TextField()
    problem_set = models.ForeignKey(ProblemSet , blank=True, null=True)

class UserProfile(UserenaBaseProfile):
    user = models.OneToOneField(User, unique=True)
    course = models.ManyToManyField(Course, null = True, blank = False)

class QuestionStats(models.Model):
    rating = models.IntegerField(blank=True,null=True)
    start_time = models.DateTimeField(blank = True, null = True)
    stop_time = models.DateTimeField(blank=True, null=True)
    duration = models.DateTimeField(blank=True, null=True)
    question = models.ForeignKey(Question,null=True,blank=False)
    profile = models.ForeignKey(UserProfile,null=True,blank=False)

