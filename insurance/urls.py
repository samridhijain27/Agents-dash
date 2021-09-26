from django.urls import path
from .views import (InsuranceListView, InsuranceUpdateView,detail_insurance_view,
                    search_insurance_cust,cust_insurance_details,get_chart_data,
                    Chart_Data_API,
                    SearchResultsView,InsuranceCreateView,InsuranceUpdateView)

urlpatterns = [    
    path('', InsuranceListView.as_view(), name='insurance-home'),
    path('insurance/<int:policy_id>/', detail_insurance_view, name='insurance-detail'),
    path('insurance/new/', InsuranceCreateView.as_view(), name='insurance-create'),
    path('insurance/<int:pk>/update/', InsuranceUpdateView.as_view(), name='insurance-update'),
    path('insurance/search/', SearchResultsView.as_view(), name='search_results'), 
    path('insurance/<int:policy_id>/customers/search/', search_insurance_cust, name='insurance-cust-search'),
    path('insurance/<int:year>/trend/api', Chart_Data_API.as_view(), name='insurance-trend'),
    path('insurance/trend', get_chart_data, name='insurance-trend-view'),
    path('customers/<int:cust_id>/policylist/', cust_insurance_details, name='cust-insurance-list'), 
]
