from django.contrib import admin

from employees.models import Employee, Skill


# Register your models here.

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'years_of_experience', 'profession', ]


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name']
