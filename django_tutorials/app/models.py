"""
Definition of models
"""

from django.db import models
from django import forms
"""
Classes to be used
""" 
class Artist(models.Model):
    name = models.CharField("artist", max_length=50)
    year_formed = models.PositiveIntegerField()
    
class ArtistForm(forms.ModelForm):
  class Meta:
    model = Artist
    fields = ['name', 'year_formed']

class ArtistForm(forms.ModelForm):
  class Meta:
    model = Artist
    fields = ['name', 'year_formed']

class Album(models.Model):
    name = models.CharField("album", max_length=50)
    artist = models.ForeignKey(Artist)