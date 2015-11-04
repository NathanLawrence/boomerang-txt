from django.db import models

# Create your models here.

class User(models.Model):
	name = models.CharField(max_length = 60)
	phone_number = models.CharField(max_length = 12) 

	def __str__(self):
		return self.name + " (" + self.phone_number + ")"

class SimpleMSG(models.Model):
	message = models.CharField(max_length = 140)
	creation_date = models.DateTimeField('date added', null=True)
	delivery_date = models.DateTimeField('date to deliver')
	author = models.ForeignKey(User, related_name = "simple_author")
	recipient = models.ForeignKey(User, related_name = "simple_recipient")

	def __str__(self):
		return self.message

class RepeatMSG(models.Model):
	message = models.CharField(max_length = 140)
	creation_date = models.DateTimeField('date added', null=True)
	delivery_interval = models.IntegerField('delivery interval in minutes')
	author = models.ForeignKey(User,related_name = "repeat_author")
	recipient = models.ForeignKey(User, related_name = "repeat_recipient")

	def __str__(self):
		return self.message