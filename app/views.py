import urllib

from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from app.forms import ReviewForm
from app.models import Product, Category, Article, Subcategory, Review


def index_view(request):
    template_name = 'app/index.html'
    products = Product.objects.all()
    articles = Article.objects.all().prefetch_related('products').order_by('date')

    context = {
        'product_list': products,
        'articles': articles,
    }
    return render(request, template_name, context)


def category_view(request, slug):
    template_name = 'app/catalog.html'
    try:
        category = Category.objects.get(slug__exact=slug)
    except ObjectDoesNotExist:
        category = Subcategory.objects.get(slug__exact=slug)

    category_products = category.products.all()

    paginator = Paginator(category_products, 3)
    current_page = request.GET.get('page', 1)
    products = paginator.get_page(current_page)
    url = '/catalog/' + slug

    prev_page, next_page = None, None
    prev_page_url, next_page_url = None, None

    if products.has_previous():
        print('prev')
        prev_page = products.previous_page_number()
        # url предыдущей страницы
        pp = {'page': prev_page}
        url_page = urllib.parse.urlencode(pp)
        prev_page_url = url + '?' + url_page
    if products.has_next():
        print('next')
        next_page = products.next_page_number()
        # url следующей страницы
        np = {'page': next_page}
        url_page = urllib.parse.urlencode(np)
        next_page_url = url + '?' + url_page

    return render(request, template_name, context={
        'category': category,
        'category_products': products,
        'current_page': current_page,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url,
    })


def product_view(request, pk):
    template_name = 'app/phone.html'
    product = get_object_or_404(Product, id=pk)
    reviews = Review.objects.filter(product=product.id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            Review.objects.create(mark=cleaned_data['mark'], name=cleaned_data['name'], content=cleaned_data['content'], product=product)
        else:
            print(form.errors)
    context = {
        'form': ReviewForm,
        'reviews': reviews,
        'product': product,
    }
    return render(request, template_name, context)
