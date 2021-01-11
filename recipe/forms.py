from django import forms
from .models import Recipe
from django.forms import ModelForm, CheckboxSelectMultiple


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ('title', 'image', 'description', 'tags', 'cooking_time')
        widgets = {
            'tag': CheckboxSelectMultiple(),
        }
