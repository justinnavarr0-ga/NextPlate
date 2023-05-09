from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Recipe
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

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

class RecipeDetail(DetailView):
    model = Recipe

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

class SavedRecipes(ListView):
    model = Recipe
    template_name = 'main_app/saved_list.html'

    

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