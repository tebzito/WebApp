"""
Definition of models
"""

from django.db import models
from django.db.models import Sum

class Poll(models.Model):
    """A poll object for use in the application views and repository."""
    text = models.CharField(max_length=200)
    pub_date = models.DateTimeFiled('date published')
    
    def total_votes(self):
        """Calculates the total number votes for this poll."""
        return self.choice_set.aggregate(Sum('votes'))['votes__sum']
        
    def __unicode__(self):
        """Return a string representation of a poll."""
        return self.text
        
class Choice(models.Model):
    """A choice poll object for use in the application views and repository."""
    poll = models.ForeignKey(Poll)
    text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def votes_percentage(self):
        """Calculates the percentage of votes for this choice."""
        total = self.poll.total_votes()
        return self.votes / float(total) * 100 if total > 0 else 0
        
    def __unicode__(self):
        
