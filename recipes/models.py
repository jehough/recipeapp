from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=200)
    instructions = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    

class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    amount = models.CharField(max_length=50)
    shoppingList = models.BooleanField(default=False)
    recipe = models.ForeignKey(to=Recipe, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.name

