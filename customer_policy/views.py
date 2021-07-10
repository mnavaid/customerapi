from django.shortcuts import render
from rest_framework import generics
from rest_framework.filters import SearchFilter
from .serializers import (PolicySerializer, CustomerPolicySerializer)
from .models import (Policy, CustomerPolicy)
#
# Create your views here.

# Create Policy Quote class

class PolicyDetailAPIView(generics.RetrieveAPIView):
    queryset = Policy.objects.all()
    serializer_class = PolicySerializer
    lookup_field = 'age'

class PolicyListAPIView(generics.ListAPIView):
    queryset = Policy.objects.all()
    serializer_class = PolicySerializer
    filter_backends= [SearchFilter]
    search_fields = ['type']

class CustomerPolicyCreateAPIView(generics.CreateAPIView):
    model=CustomerPolicy
    serializer_class = CustomerPolicySerializer
