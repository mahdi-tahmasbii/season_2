from django.contrib.auth import views
from django.urls import path
from .views import ProductList, ProductGallery, ProductCreator, ProductCreatorGallery, ProductCreatorUpdate, \
    ProductCreatorGalleryUpdate, ProductDeleteView, ProductGalleryDeleteView, user_register, Profile

app_name = 'account'
urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', user_register, name='register'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('profile/', Profile.as_view(), name="profile"),
    #
    # path('password_change/', views.PasswordChangeView.as_view(), name='password_change'),
    # path('password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    #
    # path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
    # path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
urlpatterns += [
    path('', ProductList.as_view(), name='home'),
    path('gallery/', ProductGallery.as_view(), name='gallery'),
    path('product/create', ProductCreator.as_view(), name='productcreator'),
    path('product/create/<int:pk>', ProductCreatorUpdate.as_view(), name='productupdate'),
    path('product/create/gallery', ProductCreatorGallery.as_view(), name='productcreatorgallery'),
    path('product/create/gallery/<int:pk>', ProductCreatorGalleryUpdate.as_view(), name='productgalleryupdate'),
    path('product/delete/<int:pk>', ProductDeleteView.as_view(), name='productdelete'),
    path('product/delete/gallery/<int:pk>', ProductGalleryDeleteView.as_view(), name='productgallerydelete'),
]
