from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe, Ingredient
from .forms import RecipeForm, RecipeEditForm, IngredientForm
from django.views.generic import FormView
from django.http import JsonResponse
from .mixins import AjaxFormMixin
import json

# Create your views here.
def index(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/recipes_index.html', {'recipes': recipes})

def show(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipes/recipes_show.html', {'recipe': recipe})

def new(request):
    if request.method == "POST":
        print(request.POST)
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

def add_ingredient(request, pk):
    data = json.loads(request.body)
    recipe = get_object_or_404(Recipe, pk=pk)
    print(data["amount"])
    ing = Ingredient(name=data["name"], amount= data["amount"], recipe= recipe)
    ing.save()
    return JsonResponse({"id": ing.pk,
                         "name": ing.name,
                         "amount": ing.amount})


def delete_ingredient(request):
    data = json.loads(request.body)
    ingredient = get_object_or_404(Ingredient, pk=data["ing_id"])
    ingredient.delete()
    return JsonResponse({"message":"successful"})