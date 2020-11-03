from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Tag(models.Model):
    style_color = models.CharField(max_length=200, blank=True, null=True)
    name =  models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    dimension = models.CharField(max_length=200, null=True, blank=True) #измерения, размер

    def __str__(self):
        return self.title

class Recipe(models.Model):
    #модель рецепта
    title = models.CharField(max_length=200, verbose_name='Название рецепта')
    ingredient = models.ManyToManyField(Ingredient, through='Amount', through_fields=('recipe', 'ingredient'))  
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_recipe')
    tag = models.ManyToManyField(Tag)
    duration = models.IntegerField(default=1, verbose_name='Время пиготовления') #продолжительность 
    description = models.TextField()#описание
    image = models.ImageField(upload_to='recipes/')#образ
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    slug = models.SlugField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date']

class Amount(models.Model): 
    # 
    units = models.IntegerField(default=1) #единицы
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='ingredient')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return self.ingredient.dimension

class FollowUser(models.Model):
    #модель подписки пользователей на авторов
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower') #который подписывается
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following') #на кого подписываются

    def __str__(self):
        return self.user.username

class FollowRecipe(models.Model):
    #модель подписка на рецепт
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follow_recipe_by') #клиент который сохраняет рецепт
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='follow_recipe') #рецепт который сохраняют

    def __str__(self):
        return self.recipe.title

class ShopList(models.Model):
    #список продуктов
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return self.recipe.title