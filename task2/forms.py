from django import forms
from .models import Information
 
class MyForm(forms.ModelForm):
  class Meta:
    model = Information
    fields = ["fullname", "email", "mobile_number","location","company_name","brand","clint_type","avg_Revenue",]
    labels = {
        'fullname': "Name",
        'email': "Email ID",
        "mobile_number": "Mobile Number",
        'location': "Location",
        'company_name': "Company Name",
        'brand': "Brand",
        'clint_type': "Clint Type",
        'avg_Revenue': "Average Revenue",
        }