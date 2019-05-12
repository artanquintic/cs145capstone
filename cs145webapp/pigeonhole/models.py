from django.db import models

# Create your models here.
class Pigeonhole(models.Model):
	p_number = models.IntegerField()
	item = models.BooleanField(default=False)

	def __str__(self):
		return str(self.p_number)

class Owner(models.Model):
	name = models.CharField(max_length = 100)
	email = models.EmailField()
	idNo = models.IntegerField(max_length = 9)
	pigeonhole = models.OneToOneField(Pigeonhole, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class PigeonholeAction(models.Model):
	id_number = models.IntegerField(null=True)
	name = models.CharField(max_length = 100, null=True)
	p_number = models.IntegerField()
	timestamp = models.DateTimeField()

	def __str__(self):
		return str(self.p_number)

