from django import forms
from .models import Recipe, Ingredient

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('title',)
        
class RecipeEditForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('title', 'instructions')

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ('amount', 'name')