__author__ = 'Sylvestre'
from django.shortcuts import render,render_to_response,HttpResponse
from django.template import RequestContext

def index(request):
    context = RequestContext(request)

    return render_to_response('index.html',context)
