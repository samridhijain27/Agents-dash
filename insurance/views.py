from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,CreateView,UpdateView
from .models import Insurance,Customer_Insurance
from .forms import InsuranceForm
from django.db.models import Count
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models.functions import ExtractMonth

# Create your views here.

#Insurance Create 
class InsuranceCreateView(CreateView):
    model=Insurance
    form_class = InsuranceForm

#Insurance Read
class InsuranceListView(ListView):
    paginate_by = 6
    model=Insurance
    template_name='insurance/home.html'
    context_object_name='insurances'
    ordering=['-premium']

#Insurance Update
class InsuranceUpdateView(UpdateView):
    model=Insurance
    form_class = InsuranceForm

#Insurance Search by id
class SearchResultsView(ListView):
    model = Customer_Insurance
    template_name = 'insurance/home.html'
    context_object_name='insurances'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        insurances = Insurance.objects.filter(policy_id=query)
        return insurances

#Customers associated with each policy_id
def search_insurance_cust(request, policy_id=None):
    cust_id= request.GET.get('q')
    selected_policy= get_object_or_404(Insurance, policy_id=policy_id)    
    customer_list=Customer_Insurance.objects.filter(insurance_id=selected_policy.policy_id).filter(customer_id=cust_id)
    context={
        'insurance': selected_policy,
        'customers': customer_list
        }
    return render (request, 'insurance/insurance_detail.html', context)

#Insurance details view
def detail_insurance_view(request, policy_id=None):
    selected_policy= get_object_or_404(Insurance, policy_id=policy_id)
    customer_list = Customer_Insurance.objects.filter(insurance_id=selected_policy.policy_id)
       
    context={
        'insurance': selected_policy,
        'customers': customer_list
        }
    return render (request, 'insurance/insurance_detail.html', context)

#List of Policies bought by each customers
def cust_insurance_details(request, cust_id):
    insurances = Customer_Insurance.objects.filter(customer_id=cust_id)
    context={
        'insurances': insurances,
        'customer_id':cust_id
    }
    return render(request,'insurance/filtered_policy.html',context)

#Trend View API
class Chart_Data_API(APIView): 
    def get(self, request,year,format=None):
        # year= request.GET.get('year')
        print(year)
        from_date=f'{year}-01-01'
        to_date=f'{year}-12-31'

        data_obj = Customer_Insurance.objects \
            .filter(date_of_purchase__range=(from_date,to_date)) \
            .annotate(month=ExtractMonth('date_of_purchase'))\
            .values('month') \
            .annotate(count=Count('insurance_id')).order_by()
        
        labels = []
        data = []
        

        for item in data_obj:
            labels.append(item['month'])
            data.append(item['count'])
        
        context={
                'labels': labels,
                'data': data,
                'year': year
                }
        return Response(context)

#Trend View
def get_chart_data(request):
    selected_year=2018
    if request.method == "POST":
        selected_year=request.POST.get('yearDropDown')
    context={
        'selected_year':selected_year
    }
    return render(request, 'insurance/trend.html',context)