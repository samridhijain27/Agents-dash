from django import forms

from .models import Insurance

class InsuranceForm(forms.ModelForm):
    class Meta:
        model=Insurance
        fields = ['policy_id', 'fuel','vehicle_segment','premium','bodily_injury_liability','personal_injury_protection',
        'property_damage_liability','collision','comprehensive']
    

   