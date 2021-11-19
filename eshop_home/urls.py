from django.urls import path
from eshop_home import views

app_name = 'eshop_home'
urlpatterns = [
    path('', views.home_page, name="eshop_home"),
    path('header', views.header_page, name="header_page"),
    path('footer', views.footer_page, name="footer_page"),
]
