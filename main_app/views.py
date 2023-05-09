from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormMixin
from .models import Recipe, Ingredients
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import IngredientForm
from django.urls import reverse


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
    form_class = IngredientForm
    template_name = 'main_app/recipe_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

    def get_form(self):
        form = super().get_form()
        form.instance.recipe = self.object
        return form

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


# class IngredientAdd(CreateView):
#     model = Ingredients
#     fields = ['amount', 'name', 'measurement', 'recipe']
#     template_name = 'main_app/recipe_detail.html'

#     def form_valid(self, form):
#         recipe_id = self.kwargs['recipe_id']
#         form.instance.recipe_id = recipe_id
#         return super().form_valid(form)

#     def get_success_url(self):
#         recipe_id = self.kwargs['recipe_id']
#         return reverse('recipe_detail', recipe_id = recipe_id)

def add_ingredient(request, recipe_id):
    form = IngredientForm(request.POST)
    if form.is_valid():
        new_ingredient = form.save(commit=False)
        new_ingredient.recipe_id = recipe_id
        new_ingredient.save()
    return redirect('recipe_detail', recipe_id)


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