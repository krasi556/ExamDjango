from django.db.models import Avg
from django.shortcuts import render, get_list_or_404

from employees.models import Employee


# Create your views here.

def current_employees(request):
    obj_employees = (Employee.objects
                     .annotate(avg_rating=Avg('reviews__rating'))
                     .order_by('-avg_rating'))
    context = {
        'employees': obj_employees
    }
    return render(request, 'employees/employees-in-db.html', context)
