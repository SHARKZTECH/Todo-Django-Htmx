from django.db import models
from django.contrib.auth.models import User

class Todos(models.Model):
	author=models.ForeignKey(User,on_delete=models.CASCADE)
	item=models.CharField(max_length=300)
    

	def __str__(self):
		return self.item