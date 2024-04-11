from django.urls import path
from .views import *
urlpatterns = [
    path('product_api', ProductAPIView.as_view(), name='api_products'),
    path('product_api_detail', ProductAPI.as_view(), name='products'),
    path('product_api_create/<int:pk>/', ProductDetail.as_view(), name='products_detail')
    
]