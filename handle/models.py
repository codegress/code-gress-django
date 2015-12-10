from django.db import models

# Create your models here.
class Registration(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	email = models.EmailField()
	handle = models.CharField(max_length=20,primary_key=True)
	password = models.CharField(max_length=20)

	def __unicode__(self):
		return self.handle