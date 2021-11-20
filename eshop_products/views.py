from django.shortcuts import render, redirect
from eshop_products import models
from eshop_products import forms
from eshop_categories.models import ProductsCategory
from django.shortcuts import render, get_object_or_404


# Create your views here.

def products_list(request, slug=None):
    products = models.ProductsList.objects.all()
    categories = ProductsCategory.objects.filter(is_sub=False)
    if slug:
        category = get_object_or_404(ProductsCategory, slug=slug)
        products = models.ProductsList.objects.filter(categories=category)

    context = {
        'products': products,
        'categories': categories,

    }
    return render(request, 'products_list/products_list.html', context)


def products_detail(request, *args, **kwargs):
    selected_product_id = kwargs['productId']
    product: models.ProductsList = models.ProductsList.objects.get_by_id(selected_product_id)
    product_gallery = models.ProductsGallery.objects.filter(product_id=selected_product_id)
    comment = models.Comment.objects.all().filter(product_id=selected_product_id)

    if request.method == "POST":
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            message = form.cleaned_data.get('message')
            new_comment = models.Comment(product=product, name=name, email=email, message=message)
            new_comment.save()
            return redirect('/products')
    context = {
        'product': product,
        'gallery': product_gallery,
        'comment': comment,

    }
    return render(request, 'products_detail/products_detail.html', context)
