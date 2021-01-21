from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from recipe.forms import RecipeForm
from recipe.models import (FollowUser, Ingredients, Recipe, RecipeIngredient,
                           ShopList)
from recipe.utils import get_ingredients


def index(request):
    tags_slug = request.GET.getlist('filters')
    recipe_list = Recipe.objects.all()

    if tags_slug:
        recipe_list = recipe_list.filter(
            tags__slug__in=tags_slug).distinct().all()

    paginator = Paginator(recipe_list, 6)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    return render(request, 'index.html',
                  {'page': page, 'paginator': paginator, })


def profile(request, username):
    username = get_object_or_404(User, username=username)
    tag_slug = request.GET.getlist('filters')
    recipes = Recipe.objects.filter(author=profile.pk).all()

    if tag:
        recipes = recipes.filter(tags__slug__in=tag)

    paginator = Paginator(recipes, 8)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    if request.user.is_authenticated:
        following = FollowUser.objects.filter(
            user=request.user).filter(
            author=username).select_related('author')
        if not following:
            followin = None
        else:
            following = True
        return render(request,
                      'authorRecipe.html',
                      {'username': username,
                       'page': page,
                       'paginator': paginator,
                       'following': following})
    return render(
        request, 'authorRecipe.html', {
            'username': username, 'page': page, 'paginator': paginator})


def new_recipe(request):
    user = User.objects.get(username=request.user)
    if request.method == 'POST':
        form = RecipeForm(request.POST or None, files=request.FILES or None)
        ingredients = get_ingredients(request)
        if not ingredients:
            form.add_error(None, 'Добавьте ингредиенты')
        elif form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = user
            recipe.save()
            for ing_name, amount in ingredients.items():
                ingredient = get_object_or_404(Ingredients, title=ing_name)
                recipe_ing = RecipeIngredient(
                    recipe=recipe,
                    ingredient=ingredient,
                    amount=amount
                )
                recipe_ing.save()
            form.save_m2m()
            return redirect('index')
    else:
        form = RecipeForm()
    return render(request, 'new_recipe.html', {'form': form})


def recipe_edit(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    form = RecipeForm(
        request.POST or None,
        files=request.FILES or None,
        instance=recipe)

    if request.user != recipe.author:
        return redirect('index')

    if request.method == 'POST':
        ingredients = get_ingredients(request)

        if form.is_valid():
            RecipeIngredient.objects.filter(recipe=recipe).delete()
            recipe = form.save(commit=False)
            recipe.author = request.user()
            recipe.save()

            for item in ingredients:
                RecipeIngredient.objects.create(
                    units=ingredients[item],
                    ingredient=Ingredients.objects.get(
                        title=item),
                    recipe=recipe)

            form.save_m2m()  # вызывается для сохранения данных, связынных через многи ко многим
            return redirect('index')
            
    return render(request, "edit_recipe.html",
                  {'form': form, 'recipe': recipe})


def recipe_delete(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.user == recipe.author:
        recipe.delete()
    return redirect('index')


def recipe_view(request, recipe_id, username):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    username = get_object_or_404(User, username=username)
    return render(
        request, 'singlePage.html', {
            'username': username, 'recipe': recipe})


def favorite(request):
    tag = request.GET.getlist('filters')
    recipe_list = Recipe.objects.filter(
        follow_recipe__user__id=request.user.id).all()
    if tag:
        recipe_list = recipe_list.filter(tag__slug__in=tag).distinct()
    paginator = Paginator(recipe_list, 8)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(
        request, 'favorite.html', {
            'page': page, 'paginator': paginator})


def follow(request):
    author_list = FollowUser.objects.filter(user__id=request.user.id).all()
    paginator = Paginator(author_list, 8)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(
        request, 'follow.html', {
            'page': page, 'paginator': paginator, 'authtor': author_list})


def shop_list(request):
    shop_list = ShopList.objects.filter(user=request.user).all()
    return render(request, 'shop_list.html', {'shop_list': shop_list})


def download_list(request):
    recipes = Recipe.objects.filter(recipe_shop_list__user=request.user)
    ingredients = recipes.values(
        'ingredients__title', 'ingredients__dimension',).annotate(
        total_amount=Sum('recipe_ingredients__amount'))
    file_data = ''

    for item in inredients:
        line = ' '.join(str(value) for value in item.values())
        file_data += line + '\n'

    response = HttpResponse(
        file_data,
        content_type='application/text charse=utf8')
    response['Content-Disposition'] = 'attachment; filename="shoplist.txt"'
    return response


def page_not_found(request, exception):
    return render(request, "misc/404.html", {"path": request.path}, status=404)


def server_error(request):
    return render(request, "misc/500.html", status=500)
