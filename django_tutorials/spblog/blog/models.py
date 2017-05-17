from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
	title = models.CharField(blank=True, max_length=256)
	body = models.TextField(blank=True)
	author = models.ForeignKey(User)

	def __unicode__(self):
		return u"%s" % (self.title, )
