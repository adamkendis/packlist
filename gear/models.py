from django.db import models
from django.utils import timezone

# Create your models here.

class Item(models.Model):
	item_name = models.CharField(max_length=30)
	weight_oz = models.FloatField()

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def item_info(self):
		return '{}  {}'.format(self.item_name, self.weight_oz)

	def __str__(self):
		return self.item_info()