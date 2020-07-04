from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db import models


# STORAGE = FileSystemStorage(location=settings.STATIC_ROOT)


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Модель', blank=False, null=False)
    img = models.FileField(upload_to='products/%Y/%m/%d/')
    description = models.TextField(max_length=150, verbose_name='Описание', default='')
    price = models.FloatField(verbose_name='Цена', blank=False, null=False)

    # slug = models.CharField(max_length=100)
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Категория', blank=False, null=False)
    products = models.ManyToManyField(Product, blank=True, related_name='category')
    slug = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    name = models.CharField(max_length=50, verbose_name='Подкатегория', blank=False, null=False)
    products = models.ManyToManyField(Product, blank=True, related_name='subcategory')
    category = models.ForeignKey(Category, on_delete='SET_NULL', related_name='subcategory')
    slug = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок', blank=False, null=False)
    text = models.TextField(max_length=1000, verbose_name='Текст', default='')
    products = models.ManyToManyField(Product, verbose_name='Продукты', related_name='articles')
    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title
