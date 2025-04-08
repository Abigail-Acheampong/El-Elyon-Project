from django import forms
from .models import Fee

class FeeForm(forms.ModelForm):
    class Meta:
        model = Fee
        fields = ['grade', 'amount']
