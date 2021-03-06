import django_filters
from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render, redirect
from eshop_products import models
from eshop_products import forms
from eshop_categories.models import ProductsCategory
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from account.mixins import AuthorAccessProductMixin
from django.contrib.auth.decorators import login_required
from eshop_tags.models import Tag
from django.db.models import Count


# Create your views here.
from products_order.forms import UserNewOrderForm


def products_list(request, slug=None):
    products = models.ProductsList.objects.all()[:9]
    paginator = Paginator(products, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    categories = ProductsCategory.objects.filter(is_sub=False)
    if slug:
        category = get_object_or_404(ProductsCategory, slug=slug)
        products = models.ProductsList.objects.filter(categories=category)
    tag = Tag.objects.all()
    filter = models.ProductFilter(request.GET, queryset=models.ProductsList.objects.all())
    latest_products = models.ProductsList.objects.order_by('-id').all()[:3]
    context = {
        'products': products,
        'categories': categories,
        'tag': tag,
        'page_obj': page_obj,
        'filter': filter,
        'latest_products': latest_products,
    }

    return render(request, 'products_list/products_list.html', context)


def product_tag(request, slug):
    products = models.ProductsList.objects.all()
    tag = Tag.objects.all()
    if slug:
        tags = get_object_or_404(Tag, slug=slug)
        products = models.ProductsList.objects.filter(tag=tags)
    categories = ProductsCategory.objects.filter(is_sub=False)
    context = {
        'tag': tag,
        'products': products,
        'categories': categories,
    }
    return render(request, 'products_list/products_list.html', context)


def products_detail(request, *args, **kwargs):
    selected_product_id = kwargs['productId']
    new_order_form = UserNewOrderForm(request.POST or None, initial={'product_id': selected_product_id})
    product: models.ProductsList = models.ProductsList.objects.get_by_id(selected_product_id)
    product_gallery = models.ProductsGallery.objects.filter(product_id=selected_product_id)
    related_products = models.ProductsList.objects.get_queryset().filter(categories__products=product).distinct()
    ip_address = request.user.ip_address
    if ip_address not in product.hits.all():
        product.hits.add(ip_address)

    context = {
        'product': product,
        'gallery': product_gallery,
        'related_products': related_products,
        'new_order_form': new_order_form,
    }
    return render(request, 'products_detail/products_detail.html', context)


@login_required
def products_preview(request, pk):
    if request.user.is_superuser or request.user.is_author:
        product: models.ProductsList = models.ProductsList.objects.get(pk=pk)
        product_gallery = models.ProductsGallery.objects.filter(pk=pk)
        context = {
            'product': product,
            'gallery': product_gallery,
        }
        return render(request, 'products_detail/product_preview.html', context)
    else:
        raise Http404('Not For You')


class SearchProductsView(ListView):
    template_name = 'products_list/products_list.html'
    paginate_by = 9
    context_object_name = 'products'

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q')
        if query is not None:
            return models.ProductsList.objects.search(query)

        return models.ProductsList.objects.all()
