from __future__ import unicode_literals

from django.db import models

from django.utils import timezone
# Create your models here.

class Author(models.Model):
	name = models.CharField(max_length=50)
	age = models.IntegerField()
	def __unicode__(self):
		return self.name

class Article(models.Model):
	title = models.CharField(max_length=50,default='title')
	content = models.TextField()
	counter = models.IntegerField(default=0)
	author = models.ForeignKey(Author)

	def __unicode__(self):
		return self.title
						
		
