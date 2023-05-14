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
  path('recipes/<int:pk>/add_photo/', views.add_photo, name='add_photo'),
  path('recipes/find/', views.findRecipes, name='find_recipes'),
  path('recipes/find/<str:query>', views.foundRecipe, name='recipe'),
  
#  Add Instruction to a recipe
  path('recipes/<int:recipe_id>/instructions/', views.InstructionsList.as_view(), name='instructions_list'),
  path('recipes/<int:recipe_id>/instructions/instruction_create/', views.InstructionCreate.as_view(), name='instruction_create'),
  path('recipes/<int:recipe_id>/instructions/<int:pk>/', views.InstructionDetail.as_view(), name='instruction_detail'),
  path('recipes/<int:recipe_id>/instructions/<int:pk>/instruction_delete/', views.RemoveInstruction.as_view(), name='delete_instruction'),
  
  

#   Add ingredients to a Recipe M:M
  path('recipes/<int:recipe_id>/ingredients/', views.RecipeIngredientList.as_view(), name='recipeingredients_list'),
  path('recipes/<int:recipe_id>/ingredients/add_ingredient/', views.RecipeIngredientAdd.as_view(), name='ingredient_add'),  
  path('recipes/<int:recipe_id>/ingredients/<int:pk>/', views.RecipeIngredientDetail.as_view(), name='ingredient_detail'),
  path('recipes/<int:recipe_id>/ingredients/<int:pk>/edit_ingredient/', views.RecipeIngredientEdit.as_view(), name='ingredient_edit'),  
  path('recipes/<int:recipe_id>/ingredients/<int:pk>/remove_ingredient/', views.RecipeIngredientRemove.as_view(), name='ingredient_remove'),
  path('accounts/signup/', views.signup, name='signup'),



#   My Recipes  
  path('recipes/myrecipes/', views.PersonalList.as_view(), name='personal_list'),
#   Saved Recipes  
  path('recipes/savedrecipes/', views.SavedList.as_view(), name='savedrecipes_list'),
  path('recipes/find/<str:query>/savedrecipes/create', views.SaveThisRecipe.as_view(), name='savedrecipes_create'),
  path('recipes/savedrecipes/<int:pk>/', views.SavedRecipeDetail.as_view(), name='savedrecipes_detail'),
  path('recipes/savedrecipes/<int:pk>/delete/', views.DeleteSavedRecipe.as_view(), name='savedrecipes_delete'),
  path('recipes/savedrecipes/<int:pk>/create/', views.CreateFromSaved.as_view(), name='createfromsaved'),

]