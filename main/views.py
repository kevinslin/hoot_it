# Url Shortcuts
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect, Http404
# Authentication
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from userena.forms import SignupForm
from models import *


def index(request):
    return render_to_response("main/index.html", {},
                    context_instance = RequestContext(request))

@login_required(login_url = "/")
def home(request):
    current = []
    prev = []
    courses = request.user.get_profile().course.all()
    for c in courses:
        for p in c.problemset_set.all():
            if p.current: current.append(p)
            else: prev.append(p)
    return render_to_response("main/home.html", {
        'current':current,
        'prev':prev
        },
        context_instance = RequestContext(request))

def landing_page(request):
    return render_to_response("main/landing_page.html", {
        'form':SignupForm()
        },
        context_instance = RequestContext(request))

def pset(request):
	return render_to_response("main/pset.html", {},
					context_instance = RequestContext(request))

def example(request):
    """
    Demonstration of various django commands
    """
    return render_to_response("main/example.html", {},
                    context_instance = RequestContext(request))
