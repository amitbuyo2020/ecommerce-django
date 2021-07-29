from django.shortcuts import render, get_object_or_404
from .models import Product

def home(request):
    products = Product.objects.all()

    context = {
        'products': products,
    }
    return render(request, 'Products/home.html', context)


def product_detail(request, pk):
    product = get_object_or_404(Product, id=pk)

    context = {
        'product': product
    }

    return render(request, 'Products/product-detail.html', context)