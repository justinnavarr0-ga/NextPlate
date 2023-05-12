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
    ('pieces', 'pieces'),
)



class Recipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ingredients = models.ManyToManyField('Ingredients', through='RecipeIngredients')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('recipe_detail', kwargs={'pk': self.id})


class Ingredients(models.Model):
    name = models.CharField(max_length=50)
    amount = models.FloatField()
    measurement = models.CharField(max_length=6, choices=MEASUREMENTS, default=MEASUREMENTS[0][0])
    
    def __str__(self):
        return self.name


class RecipeIngredients(models.Model):
    name = models.CharField(max_length=50, blank=True)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredients, on_delete=models.CASCADE, null=True)
    amount = models.FloatField()
    measurement = models.CharField(max_length=6, choices=MEASUREMENTS, default=MEASUREMENTS[0][0])

    def __str__(self):
        return f"{self.amount} {self.measurement} of {self.name}"
    
    def save(self, *args, **kwargs):
        # Check if the ingredient with the given name already exists in the database
        ingredient = Ingredients.objects.create(name=self.name, amount=self.amount, measurement=self.measurement)
        self.ingredient = ingredient
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('ingredient_detail', kwargs={'pk': self.id})

class RecipeInstructions(models.Model):
    step = models.IntegerField()
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    directions = models.TextField(max_length=250)
    objects = models.Manager()
    def __str__(self):
        return self.directions
        
    def get_absolute_url(self):
        return reverse('instruction_detail', kwargs={'pk': self.id})
    
class Photo(models.Model):
    url = models.CharField(max_length=200)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for recipe_id: {self.recipe_id} @{self.url}"

    def get_absolute_url(self):
        return reverse('recipe_detail', kwargs={'recipe_id': self.id})


class SavedRecipes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipes = models.ForeignKey(
        Recipe, on_delete=models.CASCADE
    )
    def __str__(self):
        return f"{self.recipes}"

    def get_absolute_url(self):
        return reverse('savedrecipes_detail', kwargs={'pk': self.id})

