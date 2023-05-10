from django.contrib import admin
# Register your models here.
from .models import Recipe, Ingredients, SavedRecipes, RecipeIngredients

admin.site.register(Recipe)
admin.site.register(RecipeIngredients)
admin.site.register(SavedRecipes)
admin.site.register(Ingredients)
