from django.urls import path
from .views import *

app_name = 'user-order'
urlpatterns = [
    path('add-user-order', add_user_order, name='add-user-order'),
    path('open_order', user_open_order, name='user_open_order'),
    path('remove-order-detail/<detail_id>', remove_order_detail, name='remove-order-detail'),
    path('request', send_request, name='request'),
    path('verify/<order_id>', verify, name='verify'),
]