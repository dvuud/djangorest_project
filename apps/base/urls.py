from django.urls import path
from .views import *
urlpatterns = [
    path('product_api', ProductAPIView.as_view(), name='api_products'),
    path('product_api', ProductAPI.as_view(), name='products'),
    path('product_api/<int:pk>/', ProductDetail.as_view(), name='products_detail')
    
]