# Url Shortcuts
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect, Http404
# Authentication
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def index(request):
    return render_to_response("main/index.html", {},
                    context_instance = RequestContext(request))

def example(request):
    """
    Demonstration of various django commands
    """
    return render_to_response("main/example.html", {},
                    context_instance = RequestContext(request))
