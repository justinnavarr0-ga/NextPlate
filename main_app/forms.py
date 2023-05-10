from django.forms import ModelForm
from .models import RecipeIngredients, SavedRecipes

class IngredientForm(ModelForm):
    class Meta:
        model = RecipeIngredients
        fields = ['name', 'amount', 'measurement']

class SavedRecipeForm(ModelForm):
    class Meta:
        model = SavedRecipes
        fields = ['recipes']