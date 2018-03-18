from django.db import models

# Create your models here.

class Translations(models.Model):
	original_text = models.CharField(max_length = 65535)
	original_lang = models.CharField(max_length = 65535)
	translation = models.CharField(max_length = 65535)
	def __str__(self):
		return self.original_text