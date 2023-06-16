from django.shortcuts import get_object_or_404, render
from django.template import loader

from .models import Category, Product

def index(request):
    all_products_list = Product.objects.order_by('-name')
    template = loader.get_template('shop/index.html')
    context = { 'all_products_list': all_products_list }
    return render(request, 'shop/index.html', context)

def detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'shop/detail.html', {'product': product})