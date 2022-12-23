from django.contrib import admin
from .models import *
from django.contrib import admin
from django_admin_relation_links import AdminChangeLinksMixin
from django.urls import reverse
from django.utils.safestring import mark_safe 


class ProductImageInline(admin.TabularInline):
	model = ProductImage
	extra = 0

# class ProductCategoryInline(admin.TabularInline):
# 	model = ProductCategory
# 	extra = 0

class ProductAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Product._meta.fields]
	inlines = [ProductImageInline]
	list_display_links = ('name','id','description',)
	
	class Meta:
		model = Product
admin.site.register(Product, ProductAdmin)


class ProductImageAdmin(admin.ModelAdmin):
	list_display = [field.name for field in ProductImage._meta.fields]

	class Meta:
		model = ProductImage
admin.site.register(ProductImage, ProductImageAdmin)

class ProductCategoryAdmin(admin.ModelAdmin):
	
	list_display = [field.name for field in ProductCategory._meta.fields]
	
	class Meta:
		model = ProductCategory

admin.site.register(ProductCategory,ProductCategoryAdmin)



