from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, UpdateView, DetailView, CreateView, DeleteView
from eshop_products.models import ProductsList, ProductsGallery
from django.urls import reverse


# Create your views here.

class ProductList(LoginRequiredMixin, ListView):
    template_name = "registration/home.html"

    def get_queryset(self):
        if self.request.user.is_superuser:
            return ProductsList.objects.all()
        else:
            return ProductsList.objects.filter(user=self.request.user)


class ProductCreator(LoginRequiredMixin, CreateView):
    model = ProductsList
    fields = ['user', 'status', 'title', 'description', 'full_info_description', 'price', 'image', 'categories', 'tag',
              'Weight',
              'Materials', 'Dimensions', 'Other_Info']
    template_name = "registration/product-create-update.html"

    def get_success_url(self):
        return reverse('account:home')


class ProductCreatorGallery(LoginRequiredMixin, CreateView):
    model = ProductsGallery
    fields = ['title', 'image', 'product']
    template_name = "registration/product-create-gallery.html"

    def get_success_url(self):
        return reverse('account:home')
