import urllib

from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, reverse, get_object_or_404, render_to_response
from datetime import datetime
import os, sys

from app.models import Product, Category, Article, Subcategory


def index_view(request):
    template_name = 'app/index.html'
    products = Product.objects.all()
    categories = Category.objects.all().prefetch_related('subcategory')
    articles = Article.objects.all().prefetch_related('products').order_by('date')

    context = {
        'product_list': products,
        'categories': categories,
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
    categories = Category.objects.all()

    paginator = Paginator(category_products, 3)
    current_page = request.GET.get('page', 1)
    products = paginator.get_page(current_page)
    url = '/catalog/'+category.slug
    print(url)

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

    return render_to_response(template_name, context={
        'category_products': products,
        'categories': categories,
        'current_page': current_page,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url,
    })


def cart_view(request):
    template_name = 'app/cart.html'

    context = {
    }
    return render(request, template_name, context)


def product_view(request, pk):
    template_name = 'app/phone.html'
    product = get_object_or_404(Product, id=pk)
    categories = Category.objects.all()

    context = {
        'categories': categories,
        'product': product,
    }
    return render(request, template_name, context)
