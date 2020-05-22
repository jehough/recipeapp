from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/user/login")
def index(request):
    user = request.user
    shoppingList = user.ingredient_set.filter(shoppingList=True)
    return render(request, 'shoppinglist/shopping_list.html', {'shoppingList': shoppingList})