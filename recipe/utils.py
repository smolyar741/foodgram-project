class IngredientsValid:
    def __init__(self, request):
        self.data = dict(request.POST.items())
        self.repeating_elements = []
        self.items = {}

        for key in self.data:
            if 'idIngredient_' in key:
                ingr_id = self.data[key]
                ingr_id_valid = valid(ingr_id)

                ingr_number = key.lstrip('idIngredient_')
                ingr_qty = self.data.get(f'valueIngredient_{ingr_number}', '1')
                ingr_qty_valid = valid(ingr_qty)

                if ingr_id_valid not in self.items:
                    self.items[ingr_id_valid] = ingr_qty_valid
                else:
                    ingredient_obj = get_object_or_404(
                        Ingredient, pk=ingr_id_valid)
                    self.repeating_elements.append(ingredient_obj.title)

    def errors(self):
        if not self.items:
            return 'Вы не добавили ни одного ингредиента'
        if self.repeating_elements:
            elements = ', '.join(self.repeating_elements)
            return f'В рецепте дублируются ингредиенты: {elements}'
        return False

        
def get_ingredients(request):
    ingredients = {}
    for key in dict(request.POST.items()):
        if 'nameIngredient' in key:
            a = key.split('_')
            ingredients[dict(request.POST.items())[key]] = int(request.POST[
                f'valueIngredient_{a[1]}'])

    return ingredients


def food_time_filter(request, queryset):
    food = {
        'breakfast': (True, False),
        'lunch': (True, False),
        'dinner': (True, False)
    }
    food_time = request.GET.get('filter')

    if food_time in food:
        food[food_time] = (True,)

    queryset_new = queryset.filter(
        breakfast__in=food['breakfast'],
        lunch__in=food['lunch'],
        dinner__in=food['dinner'])

    return queryset_new, food_time