from django.db import models
import datetime

# Create your models here.
class Registration(models.Model):
	full_name = models.CharField(max_length=30,null=True,blank=True)
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
	sample_in_desc = models.TextField(null=True,blank=True)
	sample_out_desc = models.TextField(null=True,blank=True)
	note = models.CharField(max_length=200,null=True)
	sol = models.ForeignKey('Solution',null=True,blank=True)
	sample = models.ManyToManyField('SampleCase',blank=True)
	handle = models.ForeignKey(Registration)
	created = models.DateField(auto_now_add = True)
	modified = models.DateField(auto_now = True)

	def __unicode__(self):
		return self.statement

class Solution(models.Model):
	prob = models.ForeignKey(Problem)
	language = models.CharField(max_length=100)
	text = models.TextField()
	time = models.FloatField(null=True,blank=True)
	correct = models.BooleanField(default=False)
	created = models.DateField(auto_now_add = True)
	modified = models.DateField(auto_now = True)

	def __unicode__(self):
		return self.prob.statement

class SampleCase(models.Model):
	prob = models.ForeignKey(Problem)
	sample_in = models.TextField()
	sample_out = models.TextField()
	time = models.FloatField(null=True,blank=True)

	def __unicode__(self):
		return self.prob.statement

