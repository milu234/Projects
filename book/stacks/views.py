from .models import Category, Product
from django.shortcuts import render



def product_list(request, category_slug=None):
	category = None
	categories = Category.objects.all()
	products = Product.objects.filter(available=True)
	if category_slug:
		category = get_object_or_404(Category, slug=category_slug)
		products = product.filter(category=category)
	return render(request, 'shop/Products/list.html',{'category':category, 'categories':categories, 'products':products})

def product_detail(request, id, slug):
	product = get_object_or_404(Product, id=id, slug=slug, available=True)
	cart_product_form = CartAddProductForm()
	return render(request, 'stacks/Products/detail.html',{'product':product,'cart_product_form':cart_product_form})