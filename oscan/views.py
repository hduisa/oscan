# Create your views here.
from django.template import Context, loader
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.template import RequestContext



def main(request):
    return render_to_response('oscan/main.html',{})


def scanqueue(request):
	return render_to_response('oscan/scanqueue.html',{})


def results(request):
	return render_to_response('oscan/results.html',{})

def settings(request):
	return render_to_response('oscan/settings.html',{})