# from django import forms
# from .models import Department

# class DepartmentForm(forms.ModelForm):
#     class Meta:
#         model = Department
#         fields = '__all__'

from django import forms
from .models import Department

class DepartmentForm(forms.ModelForm):

    class Meta:
        model = Department

        fields = [
            'department_name',
            'department_code',
            'manager_name',
            'location'
        ]