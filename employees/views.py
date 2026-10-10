from types import NoneType

from django.db.models import Avg, F, Q
from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect

from employees.forms import EmployeeBase, DeleteEmployee, EditEmployee, CreateEmployee, SearchForm, SkillCreate
from employees.models import Employee, Skill
from reviews.forms import ReviewForms


# Create your views here.

def current_employees(request):
    obj_employees = (Employee.objects
                     .annotate(avg_rating=Avg('reviews__rating'))
                     .order_by(F('avg_rating').desc(nulls_last=True), )
                     )
    context = {
        'employees': obj_employees
    }
    return render(request, 'employees/employees-in-db.html', context)


def focused_employee(request, employee_id):
    get_employee = get_object_or_404(Employee.objects
                                     .annotate(avg_rating=Avg('reviews__rating'))
                                     .prefetch_related('skills')
                                     , id=employee_id)

    if request.method == 'POST':
        return leave_a_review(request, get_employee)

    review_check = False
    form = ''
    if request.GET.get('review_check'):
        form = ReviewForms(request.POST or None)
        review_check = True

    if request.GET.get('hire_check'):
        return hire_employee(request, get_employee)

    context = {
        'employee': get_employee,
        'form': form,
        'review_check': review_check
    }

    return render(request, 'employees/focused-employee.html', context)


def leave_a_review(request, get_employee):
    form = ReviewForms(request.POST)
    if form.is_valid():
        review = form.save(commit=False)
        review.employee = get_employee
        review.save()
        return redirect('employees:current-employees')
    context = {
        'employee': get_employee,
        'form': form,
        'get_check': True
    }

    return render(request, 'employees/focused-employee.html', context)


def hire_employee(request, get_employee):
    get_employee.is_available = False
    get_employee.save()
    return redirect('employees:current-employees')


def create_profile(request):
    form = CreateEmployee()
    if request.method == 'POST':
        form = CreateEmployee(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('employees:new-job')
    context = {
        'form': form
    }

    return render(request, 'employees/create-profile.html', context)


def new_job(request):
    return render(request, 'employees/redirect-to-new-job.html')


def you_would_miss_out(request):
    return render(request, 'employees/you-miss-out.html')


def edit_employee(request, employee_id):
    get_employee = get_object_or_404(Employee, id=employee_id)
    if request.method == 'POST':
        form = EditEmployee(request.POST, request.FILES, instance=get_employee)
        if form.is_valid():
            form.save()
            return redirect('employees:current-employees')
    form = EditEmployee(instance=get_employee)
    context = {
        'employee': get_employee,
        'form': form
    }
    return render(request, 'employees/edit-employee.html', context)


def delete_employee(request, employee_id):
    get_employee = get_object_or_404(Employee, id=employee_id)
    form = DeleteEmployee(instance=get_employee)
    if request.method == 'POST':
        get_employee.delete()
        return redirect('core:load-main-page')

    context = {
        'employee': get_employee,
        'form': form
    }
    return render(request, 'employees/delete-employee.html', context)


def show_skills(request):
    get_skills_and_employees = (Skill.objects
                                .prefetch_related('employees'))
    form = SearchForm(request.GET or None)
    skills_checkbox = EmployeeBase()
    employees_with_skills = Employee.objects.filter(skills__isnull=False).distinct().count()
    if request.method == 'GET' and form.is_valid():
        skill_to_search, ids = form.cleaned_data['search_field'], [int(num) for num in request.GET.getlist('skills')]
        if ids:
            get_skills_and_employees = get_skills_and_employees.filter(id__in=ids)
        if skill_to_search:
            get_skills_and_employees = get_skills_and_employees.filter(name__icontains=skill_to_search)
    if request.method == 'POST':
        pass
    context = {
        'skills_and_employees': get_skills_and_employees,
        'form': form,
        'skills_in_checkbox': skills_checkbox,
        'employees_with_skills': employees_with_skills
    }

    return render(request, 'employees/skills/skills-main-menu.html', context)


def add_skill(request):
    form = SkillCreate(request.POST or None)
    get_skills = Skill.objects.all()
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('employees:skills-menu')

    context = {
        'form': form,
        'skills': get_skills
    }
    return render(request, 'employees/skills/create-new-skill.html', context)
