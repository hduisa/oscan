# Create your views here.
from django.template import Context, loader
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.template import RequestContext
from polls.models import Poll,Choice

def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    '''
    t = loader.get_template('polls/index.html')
    c = Context({
            'latest_poll_list':latest_poll_list,
    })
    '''

    return render_to_response('polls/index.html',{'latest_poll_list':latest_poll_list})


def detail(request,poll_id):
    p = get_object_or_404(Poll,pk=poll_id)

    return render_to_response('polls/detail.html',{'poll':p},context_instance = RequestContext(request))

def results(request,poll_id):
    p = get_object_or_404(Poll,pk=poll_id)

    return render_to_response('polls/results.html',{'poll':p})

def vote(request,poll_id):
    p = get_object_or_404(Poll,pk=poll_id)
    try:
        seleceted_choice = p.choice_set.get(pk=request.POST['choice'])

    except (KeyError,Choice.DoesNotExist):

        return render_to_response("polls/detail.html",{'poll':p,'error_message':"You didn't select a choice"},context_instance = RequestContext(request))
    else:
        seleceted_choice.votes +=1
        seleceted_choice.save()
        return HttpResponseRedirect(reverse('polls.views.results',args=(p.id,)))


def bootstrap(request,poll_id):
    return render_to_response('polls/bootstrap.html',{})


def main(request):
    return render_to_response('polls/main.html',{})
    
