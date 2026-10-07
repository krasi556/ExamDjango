from django import forms

from employees.models import Employee


class EmployeeBase(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'profession', 'years_of_experience', 'bio', 'hourly_rate', 'photo',
                  'skills']
        widgets = {
            'bio': forms.TextInput(attrs={
                'placeholder': 'Short bio about yourself',
            }),
        }
        labels = {
            'bio': 'Biography'
        }
        help_texts = {
            'photo': 'Not required',
            'skills': 'Not required'
        }


class DeleteEmployee(EmployeeBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.disabled = True


class EditEmployee(EmployeeBase):
    pass


class CreateEmployee(EmployeeBase):
    pass
