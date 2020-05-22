from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe, Ingredient
from django.contrib.auth.models import User
from .forms import RecipeForm, RecipeEditForm, IngredientForm
from django.views.generic import FormView
from django.http import JsonResponse
import json
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render(request, 'recipes/home.html')

@login_required(login_url="/user/login")
def index(request):
    
    recipes = request.user.recipe_set.all()
    return render(request, 'recipes/recipes_index.html', {'recipes': recipes})

@login_required(login_url="/user/login")
def show(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipes/recipes_show.html', {'recipe': recipe})

@login_required(login_url="/user/login")
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

@login_required(login_url="/user/login")
def edit(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == "POST":
        form = RecipeEditForm(request.POST, instance=recipe)
        if form.is_valid:
            form.save()
            return redirect('recipes_show', pk = recipe.pk)
    else:
        recipe_form = RecipeEditForm(instance = recipe)
        ingredient_form = IngredientForm()
    return render(request, 'recipes/recipes_edit.html', {"recipe": recipe, "recipe_form": recipe_form, "ingredient_form": ingredient_form})


def add_ingredient(request, pk):
    data = json.loads(request.body)
    recipe = get_object_or_404(Recipe, pk=pk)
    print(data["amount"])
    ing = Ingredient(name=data["name"], amount= data["amount"], recipe= recipe, user=recipe.user)
    ing.save()
    return JsonResponse({"id": ing.pk,
                         "name": ing.name,
                         "amount": ing.amount})


def delete_ingredient(request):
    data = json.loads(request.body)
    ingredient = get_object_or_404(Ingredient, pk=data["ing_id"])
    ingredient.delete()
    return JsonResponse({"message":"successful"})

def toggle_ingredient(request):
    data = json.loads(request.body)
    print(data["ing_id"])
    ingredient = get_object_or_404(Ingredient, pk=data["ing_id"])
    if ingredient.shoppingList:
        ingredient.shoppingList = False
        ingredient.save()
    else:
        ingredient.shoppingList = True
        ingredient.save()
    return JsonResponse({"message":"successful"})