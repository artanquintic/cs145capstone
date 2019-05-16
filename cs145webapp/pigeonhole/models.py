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
	idNo = models.CharField(max_length=10)
	pigeonhole = models.OneToOneField(Pigeonhole, related_name = "owner", on_delete=models.CASCADE)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('homepage')

class PigeonholeAction(models.Model):
	id_number = models.CharField(max_length=10, null=True, blank=True)
	name = models.CharField(max_length = 100, null=True, blank=True)
	p_number = models.IntegerField()
	timestamp = models.CharField(max_length=15)

	def __str__(self):
		return str(self.p_number)

