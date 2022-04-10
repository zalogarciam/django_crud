from django.db import models

class Person(models.Model):
	first_name = models.CharField(null=False,blank=False,max_length=250)
	last_name = models.CharField(null=False,blank=False,max_length=250)
	email = models.CharField(null=False,blank=False,max_length=250)