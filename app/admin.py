from django.contrib import admin
from .models import Product, Category, Article, Subcategory, Review


class CategoryInline(admin.TabularInline):
    model = Category.products.through


class SubcategoryInline(admin.TabularInline):
    model = Subcategory.products.through


class ArticleInline(admin.TabularInline):
    model = Article.products.through


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ['name']
    list_filter = ('price', 'name')
    inlines = [CategoryInline]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ['name']
    inlines = [CategoryInline]


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    fields = ('title', 'text')
    list_display = ('id', 'title', 'date')
    inlines = [ArticleInline]


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    fields = ('name', 'slug', 'category')
    list_display = ('id', 'name')
    inlines = [SubcategoryInline]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'product')



#admin.site.register(Product, ProductAdmin)

