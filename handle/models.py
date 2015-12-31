from django.db import models
import datetime

# Create your models here.
class Registration(models.Model):
	full_name = models.CharField(max_length=30,null=True)
	email = models.EmailField()
	handle = models.CharField(max_length=20,primary_key=True)
	password = models.CharField(max_length=30)
	company = models.CharField(max_length=200,null=True,blank=True)
	country = models.CharField(max_length=50,null=True,blank=True)
	website = models.CharField(max_length=200,null=True,blank=True)

	def __unicode__(self):
		return self.handle

class Problem(models.Model):
	statement = models.CharField(max_length=100)
	text = models.TextField()
	category = models.CharField(max_length=100)
	sample_in_desc = models.TextField(null=True)
	sample_out_desc = models.TextField(null=True)
	note = models.CharField(max_length=200,null=True)
	sol = models.ForeignKey('Solution',null=True)
	sample = models.ForeignKey('SampleCase')
	handle = models.ForeignKey(Registration)
	created = models.DateTimeField(auto_now = True)
	modified = models.DateTimeField(auto_now_add = True)

class Solution(models.Model):
	prob = models.ForeignKey(Problem)
	language = models.CharField(max_length=100)
	text = models.TextField()
	time = models.FloatField(null=True)
	correct = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now = True)
	modified = models.DateTimeField(auto_now_add = True)

class SampleCase(models.Model):
	prob = models.ForeignKey(Problem)
	sample_in = models.TextField()
	sample_out = models.TextField()
	time = models.FloatField(null=True)

