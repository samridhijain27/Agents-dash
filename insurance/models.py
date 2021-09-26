from django.utils import timezone
from django.db import models
from django.core.validators import  MaxValueValidator
from django.db.models.deletion import RESTRICT
from django.urls import reverse

# Create your models here.
class Customer(models.Model):
    id=models.IntegerField(primary_key=True,db_index=True)
    customer_id =models.IntegerField(default=1)
    customer_gender=models.CharField(max_length=10)
    customer_income_group=models.CharField(max_length=10)
    customer_region=models.CharField(max_length=10)
    customer_marital_status=models.IntegerField(default=0)
    is_active = models.IntegerField(default=1)

    def __str__(self) -> str:
        return f'{self.customer_id}'
    
class Insurance(models.Model):
    policy_id=models.IntegerField(primary_key=True,db_index=True)
    fuel=models.CharField(max_length=50)
    vehicle_segment=models.CharField(max_length=50)
    premium=models.IntegerField(default=0,validators=[MaxValueValidator(100000)])
    bodily_injury_liability=models.IntegerField(default=0)
    personal_injury_protection=models.IntegerField(default=0)
    property_damage_liability=models.IntegerField(default=0)
    collision=models.IntegerField(default=0)
    comprehensive=models.IntegerField(default=0)

    customers= models.ManyToManyField(Customer, through='Customer_Insurance',
    related_name='customers', blank=True)

    def __str__(self) -> str:
        return f'{self.policy_id} ~ {self.premium}'

    def get_absolute_url(self):
        return reverse('insurance-detail', kwargs={'policy_id':self.policy_id})
    
class Customer_Insurance(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.RESTRICT)
    insurance=models.ForeignKey(Insurance, on_delete=RESTRICT)
    date_of_purchase=models.DateField(default=timezone.now, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('cust-insurance-list', kwargs={'cust_id':self.customer.id})   
    
