from django.urls import path
from .views import (ListCustomerAPIView, CreateCustomerAPIView)

urlpatterns = [
    path('customer_search/',ListCustomerAPIView.as_view(), name='list'),
    path('create_customer/',CreateCustomerAPIView.as_view(), name='create'),

]
