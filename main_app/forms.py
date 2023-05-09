from django.forms import ModelForm
from .models import Saved

class SavedForm(ModelForm):
    class Meta:
        model = Saved
        fields = '__all__'