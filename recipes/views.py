from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe
from .forms import RecipeForm, RecipeEditForm, IngredientForm
from django.views.generic import FormView


# Create your views here.
def index(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/recipes_index.html', {'recipes': recipes})

def show(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipes/recipes_show.html', {'recipe': recipe})

def new(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save()
            return redirect('recipe_edit', pk = recipe.pk)
    else:
        form = RecipeForm()
    return render(request, 'recipes/recipes_new.html', {"recipe_form": form})
    
def edit(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    recipe_form = RecipeEditForm(instance = recipe)
    ingredient_form = IngredientForm()
    return render(request, 'recipes/recipes_edit.html', {"recipe": recipe, "recipe_form": recipe_form, "ingredient_form": ingredient_form})
