from django.db import models
from django.urls import reverse
# from django.contrib.auth.models import User
# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    def __str__(self):
        return f'{self.name} ({self.id})'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'recipe_id': self.id})