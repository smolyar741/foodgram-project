from recipe.models import (FollowRecipe, FollowUser, Ingredients, Recipe,
                           ShopList)
from rest_framework import serializers


class IngredientsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'dimension')
        model = Ingredients

    
class PurchaseSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    recipe = serializers.StringRelatedField()

    class Meta:
        fields = '__all__'
        model = ShopList

    def validate(self, data):
        super().validate(data)
        user = self.context.get('request_user')
        recipe = self.context.get('request_recipe')
        if ShopList.objects.filter(user=user, recipe=recipe).exists():
            raise serializers.ValidationError('has already')
        return data


class FollowRecipeSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    recipe = serializers.StringRelatedField()

    class Meta:
        fields = '__all__'
        model = FollowRecipe

    def validate(self, data):
        super().validate(data)
        user = self.context.get('request_user')
        recipe = self.context.get('request_recipe')
        if FollowRecipe.objects.filter(user=user, recipe=recipe).exists():
            raise serializers.ValidationError('has already')
        return data


class FollowUserSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    author = serializers.StringRelatedField()

    class Meta:
        fields = '__all__'
        model = FollowUser

    def validate(self, data):
        super().validate(data)
        user = self.context.get('request_user')
        author = self.context.get('request_author')
        if FollowUser.objects.filter(user=user, author=author).exists():
            raise serializers.ValidationError('already follow')
        return data