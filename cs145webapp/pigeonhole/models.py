from django.db import models
from django.urls import reverse

# Create your models here.
class Pigeonhole(models.Model):
	p_number = models.IntegerField('Pigeonhole number')
	item = models.BooleanField(default=False)

	def __str__(self):
		return str(self.p_number)

	def get_absolute_url(self):
		return reverse('homepage')

class Owner(models.Model):
	name = models.CharField(max_length = 100)
	email = models.EmailField()
	idNo = models.IntegerField()
	pigeonhole = models.OneToOneField(Pigeonhole, related_name = "owner", on_delete=models.CASCADE)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('homepage')

class PigeonholeAction(models.Model):
	id_number = models.IntegerField(null=True, blank=True)
	name = models.CharField(max_length = 100, null=True, blank=True)
	p_number = models.IntegerField()
	timestamp = models.DateTimeField()
	emailed = models.BooleanField(default=False)

	def __str__(self):
		return str(self.p_number)

