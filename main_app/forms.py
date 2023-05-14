from django.forms import ModelForm
from .models import RecipeIngredients, SavedRecipes, RecipeInstructions, Recipe

class IngredientForm(ModelForm):
    class Meta:
        model = RecipeIngredients
        fields = ['name']

class InstructionForm(ModelForm):
    class Meta:
        model = RecipeInstructions
        fields = ['directions']


class SavedRecipeForm(ModelForm):
    class Meta:
        model = SavedRecipes
        fields = ['name', 'ingredients','description']

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'ingredients']