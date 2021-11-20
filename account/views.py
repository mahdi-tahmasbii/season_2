from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, UpdateView, DetailView, CreateView, DeleteView
from eshop_products.models import ProductsList, ProductsGallery
from django.urls import reverse
from .mixins import FieldsMixin, FormValidMixin, FieldsGalleryMixin, AuthorAccessProductMixin, AuthorAccessGalleryMixin, \
    SuperuserAccessMixin


# Create your views here.

class ProductList(LoginRequiredMixin, ListView):
    template_name = "registration/home.html"

    def get_queryset(self):
        if self.request.user.is_superuser:
            return ProductsList.objects.all()
        else:
            return ProductsList.objects.filter(user=self.request.user)


class ProductGallery(LoginRequiredMixin, ListView):
    template_name = "registration/gallery.html"

    def get_queryset(self):
        if self.request.user.is_superuser:
            return ProductsGallery.objects.all()
        else:
            return ProductsGallery.objects.filter(user=self.request.user)


class ProductCreator(LoginRequiredMixin, FormValidMixin, FieldsMixin, CreateView):
    model = ProductsList
    fields = ['user', 'status', 'title', 'description', 'full_info_description', 'price', 'image', 'categories', 'tag',
              'Weight',
              'Materials', 'Dimensions', 'Other_Info']
    template_name = "registration/product-create-update.html"

    def get_success_url(self):
        return reverse('account:home')


class ProductCreatorGallery(LoginRequiredMixin, FieldsGalleryMixin, FormValidMixin, CreateView):
    model = ProductsGallery
    fields = ['user', 'status', 'title', 'image', 'product']
    template_name = "registration/product-create-gallery.html"

    def get_success_url(self):
        return reverse('account:home')


class ProductCreatorUpdate(AuthorAccessProductMixin, FormValidMixin, FieldsMixin, UpdateView):
    model = ProductsList
    fields = ['user', 'status', 'title', 'description', 'full_info_description', 'price', 'image', 'categories', 'tag',
              'Weight',
              'Materials', 'Dimensions', 'Other_Info']
    template_name = "registration/product-create-update.html"

    def get_success_url(self):
        return reverse('account:home')


class ProductCreatorGalleryUpdate(AuthorAccessGalleryMixin, UpdateView):
    model = ProductsGallery
    fields = ['user', 'status', 'title', 'image', 'product']
    template_name = "registration/product-create-gallery.html"

    def get_success_url(self):
        return reverse('account:home')


class ProductDeleteView(SuperuserAccessMixin, DeleteView):
    model = ProductsList
    success_url = reverse_lazy('account:home')
    template_name = 'registration/productslist_confirm_delete.html'


class ProductGalleryDeleteView(SuperuserAccessMixin, DeleteView):
    model = ProductsGallery
    success_url = reverse_lazy('account:home')
    template_name = 'registration/productsgallery_confirm_delete.html'
