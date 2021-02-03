from .models import ShopList


def counter(request):
    if request.user.is_authenticated:
        count = ShopList.objects.filter(user=request.user).count()
    else:
        count = None
    return {'count': count}


def url_parse(request):
    """Установка фильтров в урл страницы."""

    result_str = ''
    for item in request.GET.getlist('filters'):
        result_str += f'&filters={item}'
    return {'filters': result_str}