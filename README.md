![NextPlate](https://github.com/justinnavarr0-ga/PlanOut/assets/107282884/43879cb5-9170-4288-892e-b854864efb28)
### Built by: **[Justin Navarro](https://www.linkedin.com/in/justin-navarro/)**

[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
![Maintainer](https://img.shields.io/badge/Maintainer-justinnavarr0-blue)
![Ask](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)

![Heroku](https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white)
![Bootstrap](https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![Trello](https://img.shields.io/badge/Trello-%23026AA7.svg?style=for-the-badge&logo=Trello&logoColor=white)

## What is NextPlate?
NextPlate is an innovative recipe planning app that helps you organize your weekly meals with ease. 

With NextPlate, you can quickly search and discover new recipes, save your favorites, and create custom recipes that youll be able to share with other users. 

NextPlate provides step-by-step instructions for each recipe, making it easy to cook delicious meals at home. 

Whether you're a seasoned home cook or just starting out, 

NextPlate has something for everyone. 

<br />

[## Dont wait! Click Here to figure out whats going on your **NextPlate**](https://nextplate.herokuapp.com/)

First Sign Up or Log In on NextPlate's website:

![loginNextPlate](https://github.com/justinnavarr0-ga/PlanOut/assets/107282884/94c6eb83-1b74-42ad-b065-eebe58d2c8ae)

You can either create a Recipe:

![Create a recipe](https://github.com/justinnavarr0-ga/PlanOut/assets/107282884/03c7ad5d-6fea-4f3a-92be-760667c4c93d)

Or Find One You Like:

![find recipe](https://github.com/justinnavarr0-ga/PlanOut/assets/107282884/1836da68-0494-4802-a41b-bb90cb13a901)

You can also update and add ingredients or photos to your recipe:

![create photo edit](https://github.com/justinnavarr0-ga/PlanOut/assets/107282884/9b2bd86d-77ff-4d20-aab1-7c193fee3040)


## Roadmap
NextPlates ERD / WIREFRAME : [https://whimsical.com/nextplate-PzBExzQnsziLBXRQFFd52](https://whimsical.com/nextplate-PzBExzQnsziLBXRQFFd52)
NextPlate Trello: [https://trello.com/b/puWXrEWE/nextplate](https://trello.com/invite/b/puWXrEWE/ATTIbfda3fd69d93f89c2972fc079796296cE6E3E1FE/nextplate)

NextPlate still has a lot of features to come!

**SOME FEATURES STILL IN THE DEVELOPMENT**

-Grocery Shopping List of Ingredients for the recipes you saved
-Weekly Meal Planner, Save Recipes to days you want to make them
-More Detailed Recipes
-Ratings, Comments, and Favorites on recipes

**Problems Faced**
The most difficult functional view code I had written was the one below to connect to an API containing recipes. However, this was only the beginning to the hardest problem I faced

```
def findRecipes(request):
    search = request.GET.get('q', '') 
    api_url = 'https://api.api-ninjas.com/v1/recipe?query={}'.format(search)
    response = requests.get(api_url, headers={'X-Api-Key': })
    
    if response.status_code == requests.codes.ok:
        recipelist = response.json()  # convert response to JSON object
        return render(request, 'find.html', {'recipelist': recipelist})
    else:
        return render(request, 'find.html')

def foundRecipe(request, query):
    search = query
    api_url = 'https://api.api-ninjas.com/v1/recipe?query={}'.format(search)
    response = requests.get(api_url, headers={'X-Api-Key': })
    if response.status_code == requests.codes.ok:
        recipelist = response.json()  # convert response to JSON object
        if recipelist:
            recipe = recipelist[0] # retrieve matching item in list
            title = recipe['title']  # access title key
            ingredients = recipe['ingredients']  # access ingredients key
            instructions = recipe['instructions']
            return render(request, 'recipe.html', {'title': title, 'ingredients': ingredients, 'instructions': instructions})
        else: 
            recipelist = "Sorry This Recipe No Longer Exists!"
            return render(request, 'recipe.html', {'title': recipelist})
    else:
        return render(request, 'find.html')
```

This class based view was definitely my biggest hurdle. I found it extremely difficult for me to code this since I am still relatively new to python, and the idea of it came to me on the Friday before turning in our projects since I was able to write that function to connect to an API to generate recipes the previous day. I spent a lot of time over the weekend to prepare this view and it finally worked on Sunday. It took a lot of restructuring my models in order to utilize this the way I intended to 

```
class CreateFromSaved(CreateView):
    model = RecipeIngredients
    form_class = IngredientForm

    def form_valid(self, form):
        # Get the SavedRecipes object
        saved_recipe = get_object_or_404(SavedRecipes, pk=self.kwargs['pk'])

        # Validate the form
        if form.is_valid():
            # Create a new Recipe object from the SavedRecipes object
            newrecipe = Recipe.objects.create(
                user=self.request.user,
                name=saved_recipe.name,
            )
            instructionsinlist = saved_recipe.description.split('.')
            for item in instructionsinlist:
                instruct = item.strip() 
                if instruct:  # Check if the item is not an empty string and contains non-whitespace characters
                    recipeinstruction = RecipeInstructions(directions=instruct, recipe=newrecipe)
                    recipeinstruction.save()
            # Loop through the ingredients in the saved recipe
            ingredientsinlist = saved_recipe.ingredients.split('|')
            for item in ingredientsinlist:
                strippeditem = item.strip()  # Strip whitespace from the item
                if strippeditem:  # Check if the item is not an empty string and contains non-whitespace characters
                    try:
                        # Check if a RecipeIngredients object already exists for this ingredient
                        recipeingredient = RecipeIngredients.objects.get(name=strippeditem, recipe=newrecipe)
                    except RecipeIngredients.DoesNotExist:
                        # Creates a new RecipeIngredients object
                        recipeingredient = RecipeIngredients(name=strippeditem, recipe=newrecipe)
                        recipeingredient.save()
            # Redirects to the success URL
        return super().form_valid(form)
    def get_success_url(self):
        return reverse('recipe_list')

```

Other problems I faced were styling with bootstrap. I had only used it once before for one of my other projects and it took a while for me to switch from tailwind back to bootstrap. Still I managed though.

**Authors and Acknowledgements**

Authors:
- Justin

Acknowledgements: 
- Kenneth C. (Lead Instructor)
- Matthew G. 
- Evan M.
- Payne F.

### About This Project

This is our 4th and final capstone project showcasing our programming skills. This project utilizes Python/Django and the bootstrap framework, to build a User Centric Application with CRUD functionality and Authentication using Django's built in authentication. This project is basically the epitome of my learning at General Assembly. I have learned a lot, but one of the most important things I learned was actually how to learn and especially how I learn. I would like to again thank my instructors: Ken, Matt, Payne, and Evan for getting me to this point and I owe a huge part of my future success to their patience and guidance along the way.

Written for **General Assembly Software Engineering Immersive Bootcamp**
