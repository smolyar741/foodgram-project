from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (IngredientListView, api_follow_recipe, api_follow_user,
                    api_purchase)

router = DefaultRouter()
router.register(r'ingredients', IngredientListView)

urlpatterns = [
    path('<int:recipe_id>/purchases/', api_purchase),
    path('<int:recipe_id>/favorites/', api_follow_recipe),
    path('<int:author_id>/subscriptions/', api_follow_user)
]

urlpatterns += router.urls 
