from django import forms
from .models import *

class NewEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'



        def clean_first_name(self, *args, **kwargs):
            first_name = self.cleaned_data.get('first_name')
            unique = Employee.objects.filter(first_name=first_name)
            if unique.exists():
                raise forms.ValidationError('the name already exists')

                return first_name
