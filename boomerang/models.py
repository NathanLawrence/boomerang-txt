from django.db import models

# Create your models here.

class User(models.Model):
	name = models.CharField(max_length = 60)
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], blank=True) # validators should be a list

    def __str__(self):
		return self.name + " (" + self.phone_number + ")"

class SimpleMSG(models.Model):
	message = models.CharField(max_length = 140)
	creation_date = models.DateTimeField('date added', null=True)
	delivery_date = models.DateTimeField('date to deliver')
	origin = models.CharField(max_length = 100)
	author = models.ForeignKey(User)
	recipient = models.ForeignKey(User)

	def __str__(self):
		return self.message

class RepeatMSG(models.Model):
	message = models.CharField(max_length = 140)
	creation_date = models.DateTimeField('date added', null=True)
	delivery_interval = models.IntegerField('delivery interval in minutes')
	origin = models.CharField(max_length = 100)
	author = models.ForeignKey(User)
	recipient = models.ForeignKey(User)

	def __str__(self):
		return self.message