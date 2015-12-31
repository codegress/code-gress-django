from django.db import models

# Create your models here.
class Registration(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	email = models.EmailField()
	handle = models.CharField(max_length=20,primary_key=True)
	password = models.CharField(max_length=20)
	country = models.CharField(max_length=50,default=None)

	def __unicode__(self):
		return self.handle

class Question(models.Model):
	text = models.TextField()
	category = models.CharField(max_length=100)
	answer_id = models.ForeignKey('Answer')
	testcase_id = models.ForeignKey('TestCase')
	handle = models.ForeignKey(Registration)
	created = models.DateTimeField(auto_now = True)
	modified = models.DateTimeField(auto_now_add = True)

class Answer(models.Model):
	text = models.TextField()
	question_id = models.ForeignKey(Question)
	language = models.CharField(max_length=100)
	correct = models.BooleanField(default=False)
	time = models.FloatField(blank=True,null=True)

class TestCase(models.Model):
	question_id = models.ForeignKey(Question)
	test_in = models.TextField()
	test_out = models.TextField()
	time = models.FloatField(blank=True,null=True)

