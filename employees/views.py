from django.db.models import Avg, F
from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect

from employees.models import Employee
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
    get_employee = get_object_or_404(Employee.objects.prefetch_related('skills'), id=employee_id)

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
        return redirect('core:load-main-page')
    context = {
        'employee': get_employee,
        'form': form,
        'get_check': True
    }

    return render(request, 'employees/focused-employee.html', context)


def hire_employee(request, get_employee):
    get_employee.is_available = False
    get_employee.save()
    return redirect('current-employees')
