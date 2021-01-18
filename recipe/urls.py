
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),

    path("favorite/", views.favorite, name="favorite"),
    path("follow/", views.follow, name="follow"),
    path("shop_list/", views.shop_list, name='shop_list'),
    path('download_list', views.download_list, name='download_list'),
    path("new-recipe/", views.new_recipe, name="new_recipe"),
    path('recipe/<int:recipe_id>/edit', views.recipe_edit,
         name='recipe_edit'),
    path('recipe/<int:recipe_id>/delete', views.recipe_delete,
         name='recipe_delete'),
    path("<username>/", views.profile, name="profile"),
    path("<username>/<int:recipe_id>/", views.recipe_view,
         name="recipe_view"),
    path("<username>/<int:recipe_id>/edit/", views.recipe_edit,
         name="recipe_edit"),
]
