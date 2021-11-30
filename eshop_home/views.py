from django.shortcuts import render
from eshop_categories.models import ProductsCategory
from eshop_products import models
from eshop_products.models import *
from django.views.generic import ListView

from eshop_settings.models import *


# Create your views here.


def home_page(request):
    slider = HomeSlider.objects.all()
    slider2 = HomeSlider2.objects.first()
    banner_1 = Banner_1.objects.first()
    banner_2 = Banner_2.objects.first()
    banner_3 = Banner_3.objects.first()
    banner_4= Banner_4.objects.first()
    banner_5= Banner_5.objects.first()
    most_visit_products = ProductsList.objects.order_by('-visit_count').all()
    latest_products = ProductsList.objects.order_by('-id').all()[:6]
    products = ProductsList.objects.all()
    paginate_by = 9
    context = {
        'slider': slider,
        'slider2': slider2,
        'banner_1': banner_1,
        'banner_2': banner_2,
        'banner_3': banner_3,
        'banner_4': banner_4,
        'banner_5': banner_5,
        'most_visit_products': most_visit_products,
        'latest_products': latest_products,
        'products': products,
    }
    return render(request, 'home_page/home_page.html', context)


def header_page(request):
    categories = ProductsCategory.objects.filter(is_sub=False)
    context = {
        'categories': categories
    }
    return render(request, 'shared/header.html', context)


def footer_page(request):
    context = {}
    return render(request, 'shared/footer.html', context)


class SearchProductsView(ListView):
    template_name = 'shared/header.html'
    paginate_by = 9
    context_object_name = 'products'

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q')
        if query is not None:
            return models.ProductsList.objects.search(query)

        return models.ProductsList.objects.all()
