from rest_framework import serializers
from .models import Policy, CustomerPolicy


class PolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = Policy
        fields = '__all__'

class CustomerPolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerPolicy
        fields = '__all__'

#class PolicyListSerializer(serializers.ModelSerializer):
    #url = post_detail_url
    #user = UserDetailSerializer(read_only=True)
#    class Meta:
    #    model = Policy
#        fields = '__all__'
