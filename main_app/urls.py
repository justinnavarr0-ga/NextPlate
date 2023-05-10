from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('recipes/', views.RecipesList.as_view(), name='recipe_index'),
  path('recipes/create/', views.RecipeCreate.as_view(), name='recipe_create'),
  path('recipes/<int:pk>/', views.RecipeDetail.as_view(), name='recipe_detail'),
  path('recipes/<int:pk>/update/', views.RecipeUpdate.as_view(), name='recipe_update'),
  path('recipes/<int:pk>/delete/', views.RecipeDelete.as_view(), name='recipe_delete'),

#   My Recipes  
  path('recipes/myrecipes/', views.PersonalList.as_view(), name='personal_list'),
#   Saved Recipes  
  path('recipes/savedrecipes/', views.SavedList.as_view(), name='savedrecipes_list'),
  path('recipes/savedrecipes/add_recipe', views.SavedRecipe.as_view(), name='saved_recipes_add'),
  path('recipes/savedrecipes/<int:pk>/', views.SavedRecipeDetail.as_view(), name='savedrecipes_detail'),



#   Add ingredients
  path('recipes/<int:recipe_id>/ingredients/', views.IngredientList.as_view(), name='recipeingredients_list'),
  path('recipes/<int:recipe_id>/ingredients/<int:pk>/', views.IngredientDetail.as_view(), name='ingredient_detail'),
  path('recipes/<int:recipe_id>/ingredients/add_ingredient/', views.IngredientAdd.as_view(), name='ingredient_add'),  
  path('recipes/<int:recipe_id>/ingredients/<int:pk>/edit_ingredient/', views.IngredientEdit.as_view(), name='ingredient_edit'),  
  path('recipes/<int:recipe_id>/ingredients/<int:pk>/remove_ingredient/', views.IngredientRemove.as_view(), name='ingredient_remove'),
  path('accounts/signup/', views.signup, name='signup'),
]