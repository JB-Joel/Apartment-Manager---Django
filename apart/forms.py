from django import forms
from .models import Apartment, Tenant

class DateInput(forms.DateInput):
    input_type = 'date'

class CreateAptForm(forms.ModelForm):
    class Meta:
        model = Apartment
        exclude = ('user',)

class CreateTenantForm(forms.ModelForm):
    class Meta:
        model = Tenant
        exclude = ('apt',)
        widgets = {
            'dob': DateInput(),
            'entry_date': DateInput(),
            }