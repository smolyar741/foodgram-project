import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect


from .models import Tag, Ingredient, Recipe, Amount, FollowUser, FollowRecipe, ShopList


def index(request):
    tags_slug = request.GET.getlist('filters')
    recipe_list = Recipe.objects.all()
    
    if tags_slug:
        recipe_list.filter(tags__slug__in=tags_slug).dictinct().all()

    paginator = Paginator(recipe_list, 8) # показывать по 10 записей на странице.
    page_number = request.GET.get('page') # переменная в URL с номером запрошенной страницы
    page = paginator.get_page(page_number) # получить записи с нужным смещением

    return render(request, 'indexAuth.html', {'page': page, 'paginator': paginator, })


'''def ingredients(request):
    with open('ingredients.json', 'r', encoding='utf-8') as fh:
        data = json.load(fh)

    for i in data:
        print('Новый ингридиент:',i)
        ingredient = Ingredient(title=i['title'], dimension=i['dimension'])
        ingredient.save()
    return HttpResponse('\n'.join(str(data)))'''
