from django.http import JsonResponse
from django.shortcuts import render
from .models import ProductInBasket


def in_shopcart(request):
	return_dict = dict()
	session_key =  request.session.session_key
	print(request.POST)
	data = request.POST
	product_id = data.get("product_id")
	nmb = data.get("nmb")
	new_product = ProductInBasket.objects.create(session_key=session_key,product_id=product_id, nmb = nmb)
	product_total_number = ProductInBasket.objects.filter(session_key=session_key,is_active=True).count()
	return_dict["product_total_number"] = product_total_number
	return JsonResponse(return_dict)