from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


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
    name = models.CharField(max_length=100, blank=False)
    
  
class RecipeIngredients(models.Model):
    name = models.CharField(max_length=100, blank=True)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, blank=True)
    ingredient = models.ForeignKey(Ingredients, on_delete=models.CASCADE)
    # def save(self, *args, **kwargs):
    #     # Check if the name is not an empty string
    #     if self.name.strip():
    #         # Check if the ingredient with the given name already exists in the database
    #         existing_ingredients = Ingredients.objects.filter(name=self.name)
    #         if existing_ingredients.exists():
    #             ingredient = existing_ingredients.first()
    #             self.ingredient = ingredient
    #         else:
    #             ingredient = Ingredients.objects.create(name=self.name)
    #             self.ingredient = ingredient
    #     if self.ingredient:
    #         super().save(*args, **kwargs)



class RecipeInstructions(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    directions = models.TextField(max_length=250)
    
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
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=2000)
    ingredients = models.TextField(max_length=2000)

    def get_absolute_url(self):
        return reverse('savedrecipes_list')

