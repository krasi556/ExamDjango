from django.db.models import Avg, F
from django.shortcuts import render, get_list_or_404, get_object_or_404

from employees.models import Employee


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
    if request.method == 'GET':
        pass
    context = {
        'employee': get_employee
    }

    return render(request, 'employees/focused-employee.html', context)
