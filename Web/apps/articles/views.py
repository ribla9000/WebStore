from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from products.models import *


def home(request):
	

	products_images = ProductImage.objects.filter(is_active=True, is_main=True,product__is_active=True)
	products_images_laptops = products_images.filter(product__category__id=2)
	products_images_smartphones = products_images.filter(product__category__id=3)
	products_images_new_products = products_images.filter(product__category__id=4)

	return render(request, 'articles/home.html', locals())






# def index(request):
# 	latest_articles_list = Article.objects.order_by('-pub_date')

# 	return render(request, 'articles/list.html', {'latest_articles_list': latest_articles_list})

# def detail(request, article_id):
# 	try:
# 		a = Article.objects.get( id = article_id )
# 	except:
# 		raise Http404('Страница не найдена')

# 	latest_comments_list = a.comment_set.order_by('-id')[:10]



# 	return render(request, 'articles/detail.html', {'article': a, 'latest_comments_list': latest_comments_list})

# def leave_comment(request, article_id):
# 	try:
# 		a = Article.objects.get( id = article_id )
# 	except:
# 		raise Http404('Страница не найдена')
# 	a.comment_set.create(author_name = request.POST['name'], comment_text = request.POST['text'])

# 	return HttpResponseRedirect(reverse('articles:detail', args = (a.id,))) 

