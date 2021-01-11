from django.contrib import admin

from .models import Tag, Ingredients, Recipe, RecipeIngredient, FollowUser, FollowRecipe, ShopList


class RecipeIngredientInLine(admin.TabularInline):
    model = RecipeIngredient
    extra = 1


class TagInLine(admin.TabularInline):
    model = Tag
    extra = 1


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


class IngredientsAdmin(admin.ModelAdmin):
    list_display = ('title', 'dimension')
    list_filter = ('title',)


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    list_filter = ('author', 'title')
    inlines = (RecipeIngredientInLine,)


class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ('ingredient', 'recipe', 'amount')


class FollowUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'author')
    fields = ('user', 'author')


class FollowRecipeAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe')
    fields = ('user', 'recipe')


class ShopListAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe')
    fields = ('user', 'recipe')


admin.site.register(Tag, TagAdmin)
admin.site.register(Ingredients, IngredientsAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
admin.site.register(FollowUser, FollowUserAdmin)
admin.site.register(FollowRecipe, FollowRecipeAdmin)
admin.site.register(ShopList, ShopListAdmin)
