# import datetime
from django.db import models
# from django.utils import timezone

from tinymce.models import HTMLField


class ProductCategory(models.Model):
	name = models.CharField(max_length=128,blank=True, null=True, default=None)
	is_active = models.BooleanField(default=True)

	def __str__(self):
		return "%s" % (self.name)
	class Meta:
		verbose_name = 'Категория Товара'
		verbose_name_plural = 'Категории Товаров'

class Product(models.Model):
	# models.DecimalField(max_digits=10, decimal_places=2, default=0)
	name = models.CharField(max_length=128,blank=True, null=True, default=None)
	price = models.IntegerField(default=0)
	description = models.TextField(blank=True, null=True, default=None)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	is_active = models.BooleanField(default=True)
	discount = models.IntegerField(default=None, null=True)
	category = models.ManyToManyField(ProductCategory,blank=True, null=True, default=None)
	price_with_discount = models.IntegerField(default=None,null=True)
	
	
	def __str__(self):
		return "%s %s" % (self.name, self.price)
	class Meta:
		verbose_name = 'Товар'
		verbose_name_plural = 'Товары'


	def save(self, *args, **kwargs):
		
		price = self.price
		self.price_with_discount = ((100-self.discount)/100)*self.price


		super(Product, self).save(*args, **kwargs)


class ProductImage(models.Model):
	product = models.ForeignKey(Product,blank=True, null=True,default=None, on_delete=models.DO_NOTHING, )
	image = models.ImageField(upload_to='product_images/')

	is_main = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	
	description = models.TextField(blank=True, null=True, default=None)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	


	def __str__(self):
		return "%s" % self.id
	class Meta:
		verbose_name = 'Фотография'
		verbose_name_plural = 'Фотографии'