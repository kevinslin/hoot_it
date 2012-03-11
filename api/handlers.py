import logging
from django import forms
from piston.handler import BaseHandler, AnonymousBaseHandler
from piston.utils import validate, rc, throttle
from main.models import *

sl = logging.getLogger("django.simplelogger_v")

def _get_user_for_request(request):
    """
    Get a user from given request
    Return none on failure
    """
    if request.POST.has_key("user"):
        username = request.POST['user']
    elif request.GET.has_key("user"):
        username = request.GET['user']
    else:
        return None
    try:
        user = User.objects.get(username = username)
    except Exception:
        return None
    return user

class RatingHandler(BaseHandler):
    allowed_methods = ('POST', 'GET', 'PUT', 'DELETE')
    model = QuestionStats

    def create(self, request):
        """
        Create or update rating
        """
        attrs = self.flatten_dict(request.POST)
        question = Question.objects.get(pk = attrs['question'])
        qstats, is_new  = QuestionStats.objects.get_or_create(question = question, profile = request.user.get_profile())
        qstats.rating = attrs['rating']
        qstats.save()
        return rc.CREATED

class TimerHandler(BaseHandler):
    allowed_methods = ('POST', 'GET', 'PUT', 'DELETE')
    model = QuestionStats

    def create(self, request):
        """
        Create or update rating
        """
        attrs = self.flatten_dict(request.POST)
        question = Question.objects.get(pk = attrs['question'])
        qstats, is_new  = QuestionStats.objects.get_or_create(question = question, profile = request.user.get_profile())
        duration = attrs['duration']
        qstats.duration = datetime.time(hour = duration[-3], minute= duration[-2], seconds = duration[-1])
        qstats.save()
        return rc.CREATED


#class QuestionStats(models.Model):
    #rating = models.IntegerField()
    #start_time = models.DateTimeField()
    #stop_time = models.DateTimeField()
    #question = models.ForeignKey(Question,null=True,blank=False)
    #profile = models.ForeignKey(UserProfile,null=True,blank=False)





#class WorkoutForm(forms.ModelForm):
    #class Meta:
        #model = Workout
        #exclude = ("user",)

#class WorkoutHandler(BaseHandler):
    ##CRUD
    #allowed_methods = ('POST', 'GET', 'PUT', 'DELETE')
    #model = Workout
    ##anonymous = AnonymousFooHandler

    #@classmethod
    #def content_size(self, foo):
        ##TODO(hack)
        #return 42;

    #@validate(WorkoutForm)
    #def create(self, request):
        #"""
        #Create a new workout object and return workout instance
        #"""
        #sl.debug("creating new workout...")
        #if not self.has_model():
            #return rc.NOT_IMPLEMENTED

        #attrs = self.flatten_dict(request.form.cleaned_data)
        #attrs.update(self.flatten_dict(request.POST))
        #user = _get_user_for_request(request)
        #if not user: return rc.BAD_REQUEST
        #attrs['user'] = user
        #try:
            #inst = self.model.objects.get(**attrs)
            #return rc.DUPLICATE_ENTRY
        #except self.model.DoesNotExist:
            #inst = self.model(**attrs)
            #inst.save()
            #return inst
        ##var_char = request.POST['var_char']
        ##var_int = request.POST['var_int']
        ##em = self.model(var_char = var_char, var_int = var_int)
        ##em.save()
        ##return rc.CREATED

    #def read(self, request, username):
        #"""
        #Return workouts for given user
        #@param:
        #username
        #"""
        #try:
            #user = User.objects.get(username = username)
        #except Exception:
            #return rc.BAD_REQUEST
        #return Workout.objects.all().filter(user__exact = user).filter(user__exact = user)

    #@throttle(5, 10*60) # 5 times in 10 minutes
    #def update(self, request, pk):
        #pass
        ##foo = Foo.objects.get(pk = pk)
        ##foo.var_char = request.PUT.get('var_char')
        ##foo.save()
        ##return foo

    #def delete(self, request):
        #pass


#class ArbitraryDataHandler(BaseHandler):
    #"""
    #All other requests
    #"""
    #methods_allowed = ('GET',)

    #def read(self, request):
        #return Workout.objects.all()

