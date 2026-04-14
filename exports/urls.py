from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.product_list, name='product_list'),
    path('products/<slug:slug>/', views.product_detail, name='product_detail'),
    path('factories/', views.factories_list, name='factories_list'),
    path('list-your-factory/', views.factory_request, name='factory_request'),
    path('list-your-factory/success/', views.factory_request_success, name='factory_request_success'),
    path('investor-inquiry/', views.investor_inquiry, name='investor_inquiry'),
    path('investor-inquiry/success/', views.investor_inquiry_success, name='investor_inquiry_success'),
    path('about/', views.about, name='about'),
]

