from .models import Category


def categories(request):
    categories = Category.objects.exclude(name='Аксессуары').exclude(name='Одежда').prefetch_related('subcategory')
    accessories = Category.objects.filter(name='Аксессуары').prefetch_related('subcategory')[0]
    clothes = Category.objects.get(name='Одежда')

    return {'categories': categories,
            'accessories': accessories,
            'clothes': clothes,
            }