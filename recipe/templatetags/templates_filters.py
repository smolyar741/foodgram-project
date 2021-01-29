from django import template
from recipe.models import ShopList, FollowRecipe, FollowUser, Recipe

register = template.Library()


@register.filter(name='get_filter_values')
def get_filter_values(value):
    return value.getlist('filters')


@register.filter(name='get_filter_link')
def get_filter_link(request, tag):
    new_request = request.GET.copy()
    if tag.slug in request.GET.getlist('filters'):
        filters = new_request.getlist('filters')
        filters.remove(tag.slug)
        new_request.setlist('filters', filters)
    else:
        new_request.appendlist('filters', tag.slug)
    return new_request.urlencode()


@register.filter(name='is_shop')
def is_shop(recipe, user):
    return ShopList.objects.filter(user=user, recipe=recipe).exists()


@register.filter(name='is_favorite')
def is_favorite(recipe, user):
    return FollowRecipe.objects.filter(user=user, recipe=recipe).exists()


@register.filter(name='is_follow')
def is_follow(author, user):
    return FollowUser.objects.filter(user=user, author=author).exists()


@register.filter(name='get_recipes')
def get_recipes(author):
    return Recipe.objects.select_related("author").filter(author=author)[:3]


@register.filter(name='get_count_recipes')
def get_count_recipes(author):
# Значение "3" выбрано для правильного расчета и склонения количества рецептов,
# которые будут выводиться дополнительной кнопкой количества рецептов
# у одного автора (для одного автора выводится 3 рецепта)
    count = author.recipes.count() - 3
    if count < 1:
        return False

    if count % 10 == 1 and count % 100 != 11:
        end = 'рецепт'
    elif 2 <= count % 10 <= 4 and (count % 100 < 10 or count % 100 >= 20):
        end = 'рецепта'
    else:
        end = 'рецептов'

    return f'Еще {count} {end}...'