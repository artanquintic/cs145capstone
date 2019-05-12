from django.db import models

# Create your models here.
class Pigeonhole(models.Model):
	number = models.IntegerField()
	item = models.BooleanField(default = False)

	def __str__(self):
		return str(self.number)

class Owner(models.Model):
	name = models.CharField(max_length = 100)
	email = models.EmailField()
	idNo = models.IntegerField(max_length = 9)
	pigeonhole = models.OneToOneField(Pigeonhole, on_delete=models.CASCADE)

	def __str__(self):
		return self.name
