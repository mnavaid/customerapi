from django.contrib import admin
from .models import Policy, CustomerPolicy
# Register your models here.
@admin.register(Policy)
class PolicyAdmin(admin.ModelAdmin):
    list_display=[  'id',
                    'age',
                    'ptype',
                    'premium',
                    'cover']

@admin.register(CustomerPolicy)
class CustomerPolicyAdmin(admin.ModelAdmin):
    list_display=[  'id',
                    'customer_id',
                    'policy_id',
                    'policy_status',
                    'updated_on']
