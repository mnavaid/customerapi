from django.urls import path
from .views import (PolicyDetailAPIView, PolicyListAPIView, CustomerPolicyCreateAPIView)

urlpatterns = [
    path('policy_search/',PolicyListAPIView.as_view(), name='list'),
    path('quote/<int:age>/',PolicyDetailAPIView.as_view()),
    path('quote_status/',CustomerPolicyCreateAPIView.as_view()),

]
