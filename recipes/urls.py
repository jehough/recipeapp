from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='recipes_index'),
    path('<int:pk>/', views.show, name='recipes_show'),
    path('new/', views.new, name='recipes_new'),
    path('<int:pk>/edit/', views.edit, name='recipe_edit'),
    path('<int:pk>/add_ingredient', views.add_ingredient, name="add_ingredient"),
    path('delete_ingredient', views.delete_ingredient, name="delete_ingredient"),
    path('toggle_ingredient', views.toggle_ingredient, name="toggle_ingredient")
]