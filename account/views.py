from django.shortcuts import render, redirect
from .models import User
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, UpdateView, DetailView, CreateView, DeleteView
from eshop_products.models import ProductsList, ProductsGallery
from django.urls import reverse
from .mixins import FieldsMixin, FormValidMixin, FieldsGalleryMixin, AuthorAccessProductMixin, AuthorAccessGalleryMixin, \
    SuperuserAccessMixin
from .forms import RegisterForm, ProfileForm


# Create your views here.


def user_register(request):
    if request.user.is_authenticated:
        return redirect('/')
    register_form = RegisterForm(request.POST or None)
    if register_form.is_valid():
        user_name = register_form.cleaned_data.get('user_name')
        password = register_form.cleaned_data.get('password')
        email = register_form.cleaned_data.get('email')
        User.objects.create_user(username=user_name, email=email, password=password)
        return redirect('account:login')
    context = {
        'register_form': register_form
    }
    return render(request, 'registration/register.html', context)


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


class ProductCreatorUpdate(LoginRequiredMixin, AuthorAccessProductMixin, FormValidMixin, FieldsMixin, UpdateView):
    model = ProductsList
    fields = ['user', 'status', 'title', 'description', 'full_info_description', 'price', 'image', 'categories', 'tag',
              'Weight',
              'Materials', 'Dimensions', 'Other_Info']
    template_name = "registration/product-create-update.html"

    def get_success_url(self):
        return reverse('account:home')


class ProductCreatorGalleryUpdate(LoginRequiredMixin, FieldsGalleryMixin, FormValidMixin, UpdateView):
    model = ProductsGallery
    fields = ['user', 'status', 'title', 'image', 'product']
    template_name = "registration/product-create-gallery.html"

    def get_success_url(self):
        return reverse('account:home')


class ProductDeleteView(LoginRequiredMixin, SuperuserAccessMixin, DeleteView):
    model = ProductsList
    success_url = reverse_lazy('account:home')
    template_name = 'registration/productslist_confirm_delete.html'


class ProductGalleryDeleteView(LoginRequiredMixin, SuperuserAccessMixin, DeleteView):
    model = ProductsGallery
    success_url = reverse_lazy('account:home')
    template_name = 'registration/productsgallery_confirm_delete.html'


class Profile(LoginRequiredMixin, UpdateView):
    model = User
    template_name = "registration/profile.html"
    form_class = ProfileForm
    success_url = reverse_lazy("account:profile")

    def get_object(self):
        return User.objects.get(pk=self.request.user.pk)

    def get_form_kwargs(self):
        kwargs = super(Profile, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user
        })
        return kwargs
