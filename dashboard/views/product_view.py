from django.shortcuts import render, redirect, get_object_or_404
from ..models.product_model import Product
from ..forms.product_form import ProductForm
from dashboard.models.category_model import ProductCategory
from django import forms



def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'products/product_add.html', {'form': form})

def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('product_list')

def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    
    return render(request, 'products/product_edit.html', {'form': form, 'product': product})

def publish_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.is_published = True
    product.save()
    return redirect('store')

def product_list_store(request):
    products = Product.objects.filter(is_published=True)
    return render(request, 'products/product_list.html', {'products': products})

def toggle_publish(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.is_published = not product.is_published
    product.save()
    return redirect('product_list')

def published_products(request):
    products = Product.objects.filter(is_published=True)
    return render(request, 'products/published_list.html', {'products': products})

def product_list_store(request):
    products = Product.objects.filter(is_published=True)
    return render(request, 'products/product_list_store.html', {'products': products})


def category_list(request):
    categories = ProductCategory.objects.all()
    return render(request, 'categories/category.html', {'categories': categories})

class CategoryForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = ['name']

def category_add(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'categories/category_add.html', {'form': form})
