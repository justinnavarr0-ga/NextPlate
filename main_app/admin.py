from django.contrib import admin
# Register your models here.
from .models import Recipe, Ingredients, SavedRecipes, RecipeIngredients, RecipeInstructions, Photo

admin.site.register(Recipe)
admin.site.register(RecipeIngredients)
admin.site.register(RecipeInstructions)
admin.site.register(SavedRecipes)
admin.site.register(Ingredients)
admin.site.register(Photo)