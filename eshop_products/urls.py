from django.urls import path
from eshop_products import views

app_name = 'eshop_products'
urlpatterns = [
    path('products/', views.products_list, name='products_list'),
    path('products/category/<slug:slug>/', views.products_list, name='products_list'),
    path('products/tag/<slug:slug>/', views.product_tag, name='products_tag'),
    path('products/<productId>/<name>/', views.products_detail, name='products_detail'),
    path('products/preview/<int:pk>', views.products_preview, name='products_preview'),
]
