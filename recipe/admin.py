from django.contrib import admin

from .models import Tag, Ingredient, Recipe, Amount, FollowUser, FollowRecipe, ShopList


class AmountInLine(admin.TabularInline):
    model = Amount
    extra = 1


class TagInLine(admin.TabularInline):
    model = Tag 
    extra = 1 


class TagAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug')
    empty_value_display = '-пусто-'


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'dimension')
    search_fields = ('title',)
    list_filter = ('title',)
    empty_value_display = '-пусто-'


class RecipeAdmin(admin.ModelAdmin):
    def follow_recipe_count(self, obj):
        return FollowRecipe.objects.filter(recipe=obj).count()

    follow_recipe_count.short_description = 'Краткое описание'

    list_display = ('pk', 'title', 'author', 'pub_date', 'follow_recipe_count')
    search_fields = ('title',)
    list_filter = ('pub_date',)
    inlines = (AmountInLine,)
    readonly_fields = ('follow_recipe_count',)


class AmountAdmin(admin.ModelAdmin):
    fields = ('ingredient', 'recipe', 'units')
    search_fields = ('ingredient', 'recipe')


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
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Amount, AmountAdmin)
admin.site.register(FollowUser, FollowUserAdmin)
admin.site.register(FollowRecipe, FollowRecipeAdmin)
admin.site.register(ShopList, ShopListAdmin)