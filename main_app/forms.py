from django.forms import ModelForm
from .models import RecipeIngredients, SavedRecipes, RecipeInstructions

class IngredientForm(ModelForm):
    class Meta:
        model = RecipeIngredients
        fields = [ 'amount', 'measurement', 'name']

class InstructionForm(ModelForm):
    class Meta:
        model = RecipeInstructions
        fields = [ 'step', 'directions']


class SavedRecipeForm(ModelForm):
    class Meta:
        model = SavedRecipes
        fields = ['recipes']