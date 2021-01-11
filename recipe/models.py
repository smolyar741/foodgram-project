from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Tag(models.Model):
    color = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name


class Ingredients(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    dimension = models.CharField(
        max_length=200,
        null=True,
        blank=True)  # измерения, размер

    def __str__(self):
        return self.title


class Recipe(models.Model):
    # модель рецепта
    title = models.CharField(max_length=200, verbose_name='Название рецепта')
    ingredients = models.ManyToManyField(
        Ingredients, through='RecipeIngredient')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipes_author')
    tags = models.ManyToManyField(Tag)
    cooking_time = models.IntegerField(default=1)  # продолжительность
    description = models.TextField()  # описание
    image = models.ImageField(
        upload_to='recipe/',
        blank=True,
        null=True)  # образ

    def __str__(self):
        return self.title


class RecipeIngredient(models.Model):
    #
    amount = models.IntegerField(default=1)  # единицы
    ingredient = models.ForeignKey(
        Ingredients,
        on_delete=models.CASCADE,
        related_name='recipes')
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='recipe_ingredients')

    def __str__(self):
        return self.ingredient.dimension


class FollowUser(models.Model):
    # модель подписки пользователей на авторов
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower')  # который подписывается
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following')  # на кого подписываются

    def __str__(self):
        return f'follower - {self.user} following - {self.author}'


class FollowRecipe(models.Model):
    # модель подписка на рецепт
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follow_recipe_by')  # клиент который сохраняет рецепт
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='follow_recipe')  # рецепт который сохраняют

    def __str__(self):
        return f'follower - {self.user} following recipe- {self.recipe}'


class ShopList(models.Model):
    # список продуктов
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_shopping_list')
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='recipe_shopping_list')

    def __str__(self):
        return self.recipe.title
