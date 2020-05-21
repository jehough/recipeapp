from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='recipes_index'),
    path('<int:pk>', views.show, name='recipes_show'),
    path('new/', views.new, name='recipes_new'),
    path('<int:pk>/edit', views.edit, name='recipe_edit')
]