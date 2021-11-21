from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from eshop_products.models import ProductsList, ProductsGallery
from eshop_products.models import ProductsList, ProductsCategory


class FieldsMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            self.fields = [
                'user',
                'status',
                'title',
                'price',
                'image',
                'description',
                'full_info_description',
                'categories',
                'tag',
                'Weight',
                'Materials',
                'Dimensions',
                'Other_Info',
            ]
        elif request.user.is_author:
            self.fields = [
                'title',
                'price',
                'image',
                'description',
                'full_info_description',
                'categories',
                'tag',
                'Weight',
                'Materials',
                'Dimensions',
                'Other_Info',
            ]
        else:
            raise Http404('YOU CAN`T SEE THIS PAGE')
        return super().dispatch(request, *args, **kwargs)


class FieldsGalleryMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            self.fields = [
                'user',
                'status',
                'product',
                'title',
                'image',
            ]
        elif request.user.is_author:
            self.fields = [
                'product',
                'title',
                'image',
            ]
        else:
            raise Http404('YOU CAN`T SEE THIS PAGE')
        return super().dispatch(request, *args, **kwargs)


class FormValidMixin():
    def form_valid(self, form):
        if self.request.user.is_superuser:
            form.save()
        else:
            self.obj = form.save(commit=False)
            self.obj.user = self.request.user
            self.obj.status = 'd'
        return super().form_valid(form)


class AuthorAccessProductMixin():
    def dispatch(self, request, pk, *args, **kwargs):
        product = get_object_or_404(ProductsList, pk=pk)
        if product.user == request.user and product.status in ['b', 'd'] or request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404('YOU CAN`T SEE THIS PAGE')


class AuthorAccessGalleryMixin():
    def dispatch(self, request, pk, *args, **kwargs):
        product = get_object_or_404(ProductsGallery, pk=pk)
        if product.user == request.user and product.status == ['b', 'd'] or request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404('YOU CAN`T SEE THIS PAGE')


class SuperuserAccessMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404('YOU CAN`T SEE THIS PAGE')
