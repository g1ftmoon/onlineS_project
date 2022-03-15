from django.contrib import admin

from applications.project.models import ProductImage, Category, Product


class InlineProductImage(admin.TabularInline):
    model = ProductImage
    extra = 1
    fields = ('image', )


class ProductAdminDisplay(admin.ModelAdmin):
    inlines = [InlineProductImage, ]


admin.site.register(Category)
admin.site.register(Product, ProductAdminDisplay)
