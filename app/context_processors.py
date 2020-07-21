from .models import Category


def categories(request):
    accessories = Category.objects.filter(name='Аксессуары').prefetch_related('subcategory')
    categories = Category.objects.exclude(name='Аксессуары').exclude(name='Одежда').prefetch_related('subcategory')
    clothes = Category.objects.filter(name='Одежда').prefetch_related('subcategory')

    return {'categories': categories,
            'accessories': accessories,
            'clothes': clothes,
            }