from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from ..models.category_model import ProductCategory


def category_list(request):
    categories = ProductCategory.objects.all()
    return render(request, 'dashboard/categories/category_list.html', {'categories': categories})

def category_add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            ProductCategory.objects.create(name=name)
            return redirect('category_list')
    return render(request, 'dashboard/categories/category_add.html')



def category_delete(request, category_id):
    category = get_object_or_404(ProductCategory, id=category_id)
    category.delete()
    return redirect('category_list')
def category_edit(request, category_id):
    category = get_object_or_404(ProductCategory, id=category_id)
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            category.name = name
            category.save()
            return redirect('category_list')
    return render(request, 'dashboard/categories/category_edit.html', {'category': category})

