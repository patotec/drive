
from django.db import models

class Contact(models.Model):
	name = models.CharField(max_length=200)
	email = models.EmailField()
	subject = models.CharField(max_length=2000)
	message = models.TextField()

	def __str__ (self):
		return self.name

class Team(models.Model):
	name = models.CharField(max_length=200)
	image = models.ImageField()

	def __str__ (self):
		return self.name

