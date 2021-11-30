from django.urls import path
from .views import *

app_name = 'eshop_settings'
urlpatterns = [
    path('contact-us', contact_us, name='contact_us'),
    path('about-us', about_us, name='about_us')
]
