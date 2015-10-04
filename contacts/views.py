from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from .models import Contact # '.' signifies the current directory

# Create your views here.

# def alumni(request):
#    template_name = 'alumni.html'
#    alumni_list = Contact.objects.all()
#    return render_to_response(template_name, context_instance=RequestContext(request))