from django.shortcuts import get_object_or_404, render_to_response
from django.template.context import RequestContext
from .models import Article, Content, Image, Chapter, Contributor # '.' signifies the current directory
from collections import OrderedDict
from itertools import chain
import json
from django.conf import settings
import random
from django.shortcuts import redirect
from itertools import chain
import logging

logger = logging.getLogger("magazine")

# Create your views here.
def index(request):
  template_name = 'index.html'
  return render_to_response(template_name, context_instance=RequestContext(request))

def masthead(request):
  template_name = 'about_us.html'
  return render_to_response(template_name, context_instance=RequestContext(request))

def alumni(request):
  template_name = 'alumni.html'
  return render_to_response(template_name, context_instance=RequestContext(request))