from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormMixin, FormView
from .models import Recipe, SavedRecipes, RecipeIngredients, RecipeInstructions
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import IngredientForm, SavedRecipeForm, InstructionForm
from django.urls import reverse, reverse_lazy


# Create your views here.
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')
def about(request):
  return render(request, 'about.html')
class PersonalList(ListView):
    model = Recipe
    template_name = 'main_app/personal_list.html'
    def get_queryset(self):
        # Get the current user
        user = self.request.user
        # Filter the recipes by user
        queryset = Recipe.objects.filter(user=user)
        return queryset
class RecipesList(ListView):
    model = Recipe

class RecipeDetail(FormMixin, DetailView):
    model = Recipe
    template_name = 'main_app/recipe_detail.html'
    def get_form(self):
        form_class = IngredientForm
        form = super().get_form(form_class=form_class)
        form.instance.recipe = self.object
        return form
    def get_instructform(self):
        form_class2 = InstructionForm
        instructform = super().get_form(form_class=form_class2)
        instructform.instance.recipe = self.object
        return instructform
    def get_context_data(self, **kwargs):
        print(self.object)
        context = super().get_context_data(**kwargs)
        recipe_instructions= Recipe.objects.get(id=self.object.id)
        recipe_ingredients = RecipeIngredients.objects.filter(recipe=self.object)
        context['form'] = self.get_form()
        context['instructform'] = self.get_instructform()
        context['recipeingredients'] = recipe_ingredients
        context['recipeinstructions'] = recipe_instructions
        context['savedrecipeform'] = SavedRecipeForm(initial={'recipe': self.object})
        return context



class RecipeCreate(CreateView):
    model = Recipe
    fields = ['name', 'description']
    def form_valid(self, form):
        # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user  # form.instance is the recipe
        # Let the CreateView do its job as usual
        return super().form_valid(form)
    success_url = '/recipes'
class RecipeUpdate(UpdateView):
    model = Recipe
    fields = ['name', 'description']
class RecipeDelete(DeleteView):
    model = Recipe
    success_url = '/recipes'
class RecipeIngredientList(ListView):
    model = RecipeIngredients
    template_name = 'main_app/recipeingredients_list.html'
    def get_queryset(self):
        recipe_id = self.kwargs['recipe_id']
        queryset = RecipeIngredients.objects.filter(recipe_id=recipe_id)
        return queryset
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe_id = self.kwargs['recipe_id']
        recipe = Recipe.objects.get(id=recipe_id)
        context['recipe'] = recipe
        return context
class RecipeIngredientDetail(DetailView):
    model = RecipeIngredients
    template_name = 'main_app/ingredient_detail.html'


class RecipeIngredientAdd(FormView):
    form_class = IngredientForm
    template_name = 'main_app/add_ingredient.html'
    def form_valid(self, form):
        recipe_id = self.kwargs['recipe_id']
        new_ingredient = form.save(commit=False)
        new_ingredient.recipe_id = recipe_id
        new_ingredient.save()
        return super().form_valid(form)

    def get_success_url(self):
        recipe_id = self.kwargs['recipe_id']
        return reverse('recipe_detail', kwargs={'pk': recipe_id})


class RecipeIngredientRemove(DeleteView):
    model = RecipeIngredients
    template_name = 'main_app/recipe_detail.html'
    def get_success_url(self):
        recipe_id = self.kwargs['recipe_id']
        print(self.kwargs)
        return reverse('recipe_detail', kwargs={'pk': recipe_id})
class RecipeIngredientEdit(UpdateView):
    model = RecipeIngredients
    fields = ['name', 'amount', 'measurement']
    template_name = 'main_app/edit_ingredient.html'
    def form_valid(self, form):
        recipe_id = self.kwargs['recipe_id']
        new_ingredient = form.save(commit=False)
        new_ingredient.recipe_id = recipe_id
        new_ingredient.save()
        return super().form_valid(form)
    def get_success_url(self):
        recipe_id = self.kwargs['recipe_id']
        return reverse('recipe_detail', kwargs={'pk': recipe_id})
class InstructionsList(ListView):
    model = Recipe
    template_name = 'main_app/instructions_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe_id = self.kwargs['recipe_id']
        recipe = Recipe.objects.get(id=recipe_id)
        context['object'] = recipe
        return context
class InstructionCreate(FormView):
    model = Recipe
    template_name = 'main_app/instruction_create.html'
    form_class = InstructionForm
    def form_valid(self, form):
        recipe_id = self.kwargs['recipe_id']
        new_instruction = form.save(commit=False)
        new_instruction.recipe_id = recipe_id
        new_instruction.save()
        return super().form_valid(form)
    def get_success_url(self):
        recipe_id = self.kwargs['recipe_id']
        return reverse('recipe_detail', kwargs={'pk': recipe_id})
class InstructionDetail(DetailView):
    model = RecipeInstructions
    template_name = 'main_app/instruction_detail.html'
    def get_queryset(self):
        recipe_id = self.kwargs['recipe_id']
        queryset = Recipe.objects.filter(id=recipe_id)
        print(queryset)
        return queryset
    def get_success_url(self):
        recipe_id = self.kwargs['recipe_id']
        return reverse('instruction_detail', kwargs={'pk': recipe_id})


class RemoveInstruction(DeleteView):
    model = RecipeInstructions
    form_class = InstructionForm
    template_name = 'main_app/instruction_delete.html'
    def get_queryset(self):
        recipe_id = self.kwargs['recipe_id']
        # Filter the recipes 
        queryset = Recipe.objects.filter(id=recipe_id)
        print(queryset)
        return queryset
    def get_success_url(self):
        recipe_id = self.kwargs['recipe_id']
        return reverse('recipe_detail', kwargs={'pk': recipe_id})
    




# SAVED

class SavedList(ListView):
    model = SavedRecipes
    template_name = 'main_app/savedrecipe_list.html'
    def get_queryset(self):
        # Get the current user
        user = self.request.user
        # Filter the recipes by user
        queryset = SavedRecipes.objects.filter(user=user)
        return queryset
class SavedRecipeDetail(DetailView):
    model = SavedRecipes

class SaveThisRecipe(CreateView):
    model = SavedRecipes
    form_class = SavedRecipeForm
    success_url = reverse_lazy('main_app/savedrecipes_list')

    def form_valid(self, form):
        # pre-populate the form with the recipe and the current user
        form.instance.user = self.request.user
        form.instance.recipes = Recipe.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)
    
#SAVED



def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('recipe_index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)