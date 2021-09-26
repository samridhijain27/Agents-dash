from django.contrib import admin

from .models import Customer,Insurance,Customer_Insurance
# Register your models here.

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_id', 'customer_gender', 'customer_income_group', 'customer_region', 'customer_marital_status')
    list_filter = ('customer_gender', 'customer_income_group', 'customer_region', 'customer_marital_status')
    ordering = ('customer_id',)


@admin.register(Insurance)
class InsuranceAdmin(admin.ModelAdmin):
    list_display = ('policy_id', 'fuel', 'vehicle_segment', 'premium', 'bodily_injury_liability'
    ,'personal_injury_protection','property_damage_liability','collision','comprehensive'
    )
    list_filter = ('policy_id', 'premium',)
    search_fields = ('policy_id', 'premium',)

admin.site.register(Customer_Insurance)
