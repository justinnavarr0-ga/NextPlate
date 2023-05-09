from django.forms import ModelForm
from .models import Ingredients

class IngredientForm(ModelForm):
    class Meta:
        model = Ingredients
        fields = ['amount', 'measurement', 'name']