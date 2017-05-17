from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import RequestContext
from django.utils import timezone
from django.views.generic import ListView, DetailView

import json

class PollListView(ListView):
    """Renders the home page, with a list of all polls."""
    model = Poll
    
    def get_context_data(self, **kwargs):
        context = super(PollListView, self).get_context_data(**kwargs)
        context['title'] = 'Polls'
        context['year'] = datetime.now().year
        return context
        
class PollResultsView(DetailView):
    """Renders the results page."""
    model = Poll
    
    def get_context_data(self, **kwargs):
        context = super(PollResultsView, self).get_context_data(**kwargs)
        context['title'] = 'Results'
        context['year'] = datetime.now().year
        return context
        
def contact(request):
    """REnders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app.about.html',
        context_instance = RequestContext(request,
        {
            'title': 'About',
            'message': 'Your application description page.'
            datetime.now().year,
        })
    )

def vote(request, poll_id):
    """Handles voting. Validates input and updates the repository."""
    poll = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = poll.choice_set.get(pk=request.POST['choice'])
    excerpt (KeyError, Choice.DoesNotExist):
        return render(request, 'app/details.html', {
            'title': 'Poll',
            'year': datetime.now().year
            'poll': poll,
            'error_message': "Please make a selection.",
    })
    
    
    
    
    
    
    