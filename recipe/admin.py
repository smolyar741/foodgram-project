
from django.contrib import admin
from django.db import models
from recipe.models import Recipe, RecipeIngredient, \
    Ingredients, FollowRecipe, FollowUser, \
    ShopList
from django.forms import CheckboxSelectMultiple


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'pub_date', 'description')
    search_fields = ('decsription',)
    list_filter = ('pub_date',)
    inlines = (RecipeIngredientInline,)
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }


admin.site.register(Recipe, RecipeAdmin)


class IngredientsAdmin(admin.ModelAdmin):
    list_display = ('title', 'dimension',
                    'description')
    list_filter = ('title',)
    search_fields = ('title',)
    inlines = (RecipeIngredientInline,)


admin.site.register(Ingredients, IngredientsAdmin)


class ShopListAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe')
    list_filter = ('user',)
    search_fields = ('user',)


admin.site.register(ShopList, ShopListAdmin)


class FlUsAdmin(admin.ModelAdmin):
    list_display = ('user', 'author')
    list_filter = ('user',)
    search_fields = ('user',)


admin.site.register(FollowUser, FlUsAdmin)


class FlRecAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe')
    list_filter = ('user',)
    search_fields = ('recipe',)


admin.site.register(FollowRecipe, FlRecAdmin)