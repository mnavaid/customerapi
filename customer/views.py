from django.shortcuts import render
from rest_framework import generics
from rest_framework.filters import  SearchFilter
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import (CustomerCreateSerializer, CustomerListSerializer)
from .models import Customer

# Create your views here.

# Create customer class

class CreateCustomerAPIView(generics.CreateAPIView):
    model=Customer
    serializer_class = CustomerCreateSerializer


class ListCustomerAPIView(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerListSerializer
    filter_backends= [SearchFilter]
    search_fields = ['first_name', 'last_name', 'dob']
    authentication_classes = [BasicAuthentication]
    #Global Setting is override
    permission_classes = [AllowAny]
