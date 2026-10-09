from django import forms

from employees.models import Employee, Skill


class EmployeeBase(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'profession', 'years_of_experience', 'bio', 'hourly_rate', 'photo',
                  'skills']
        widgets = {
            'bio': forms.TextInput(attrs={
                'placeholder': 'Short bio about yourself',
            }),
            'skills': forms.CheckboxSelectMultiple()
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


class BaseSkill(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name']


class SkillCreate(BaseSkill):
    class Meta(BaseSkill.Meta):
        error_messages = {
            'name': {
                'unique': 'This skill already exists, our AI invented it first '
            }
        }


class DeleteSkill(BaseSkill):
    pass


class EditSkill(BaseSkill):
    pass


class SearchForm(forms.Form):
    search_field = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Give it a try'
        })
    )
