from django.shortcuts import render
from eshop_products import models
# Create your views here.
from django.views.generic import ListView


def home_page(request):
    context = {}
    return render(request, 'home_page/home_page.html', context)


def header_page(request):
    context = {}
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
