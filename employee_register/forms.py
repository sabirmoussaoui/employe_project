from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        #fields = ['fullname']
        labels={
            'fullname':'Full name',
            'emp_code':'EMP Code'
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label="Select"
        self.fields['mobile'].required = False
