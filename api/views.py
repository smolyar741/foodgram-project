from django.contrib.auth import get_user_model
from recipe.models import (FollowRecipe, FollowUser, Ingredients, Recipe,
                           ShopList)
from rest_framework.decorators import api_view
from rest_framework.filters import SearchFilter
from rest_framework.generics import get_object_or_404
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from rest_framework.viewsets import GenericViewSet

from .serializers import (FollowRecipeSerializer, FollowUserSerializer,
                          IngredientsSerializer, PurchaseSerializer)

User = get_user_model()


class IngredientsListView(ListModelMixin, GenericViewSet):
    queryset = Ingredients.objects.all()
    serializer_class = IngredientsSerializer
    filter_backends = [SearchFilter, ]
    search_fields = ['title', ]
    ordering_fields = ['title', ]


@api_view(['POST', 'DELETE'])
def api_purchase(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)

    if request.method == 'POST':
        serializer = PurchaseSerializer(data=request.data, context={
            'request_user': request.user,
            'request_recipe': recipe})
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user, recipe=recipe)
        return Response({'success': True}, status=HTTP_201_CREATED)
    
    if request.method == 'DELETE':
        get_object_or_404(ShopList, user=request.user, recipe=recipe).delete()
        return Response({'success': True})


@api_view(['POST', 'DELETE'])
def api_follow_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)

    if request.method == 'POST':
        serializer = FollowRecipeSerializer(data=request.data, context={
            'request_user': request.user,
            'request_recipe': recipe})
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user, recipe=recipe)
        return Response({'success': True}, status=HTTP_201_CREATED)
    
    if request.method == 'DELETE':
        get_object_or_404(FollowRecipe, user=request.user, recipe=recipe).delete()
        return Response({'success': True})


@api_view(['POST', 'DELETE'])
def api_follow_user(request, author_id):
    author = get_object_or_404(User, pk=author_id)

    if request.method == 'POST':
        serializer = FollowUserSerializer(data=request.data, context={
            'request_user': request.user,
            'request_author': author})
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user, recipe=recipe)
        return Response({'success': True}, status=HTTP_201_CREATED)
    
    if request.method == 'DELETE':
        get_object_or_404(FollowUser, user=request.user, author=author).delete()
        return Response({'success': True})
