from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

MEASUREMENTS = (
    ('oz', 'ounce'),
    ('g', 'gram'),
    ('lb', 'pound'),
    ('kg', 'kilogram'),
    ('pinch', 'pinch'),
    ('l', 'liter'),
    ('gal', 'Gallon'),
    ('pint', 'Pint'),
    ('qt', 'Quart'),
    ('ml', 'Mililiter'),
    ('cup', 'Cup'),
    ('tbsp', 'tablespoon'),
    ('tsp', 'teaspoon'),
)



# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('recipe_detail', kwargs={'pk': self.id})

class Ingredients(models.Model):
    amount = models.FloatField()
    measurement = models.CharField(
        max_length=6,
        choices=MEASUREMENTS,
        default=MEASUREMENTS[0][0]
    )
    name = models.CharField(max_length=50)
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE
    )
    def __str__(self):
        return f"{self.amount} {self.get_measurement_display()}(s) of {self.name}"
    class Meta:
        ordering = ['-name']


class Saved(models.Model):
    name = models.CharField(max_length=100)
