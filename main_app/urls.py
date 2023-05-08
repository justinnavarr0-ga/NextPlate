from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('recipes/', views.RecipesList.as_view(), name='recipes_index'),
#   path('recipes/<int:recipe_id>/', views.recipes_detail, name='detail'),
]