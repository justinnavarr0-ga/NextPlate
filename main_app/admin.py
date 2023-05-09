from django.contrib import admin
# Register your models here.
from .models import Recipe, Saved

admin.site.register(Recipe)
admin.site.register(Saved)
