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
    form = ReviewForms(request.POST or None)
    get_check = False
    if request.GET.get('get_check'):
        get_check = True
    if request.method == 'POST' and form.is_valid():
        review = form.save(commit=False)
        review.employee = get_employee
        review.save()
        return redirect('core:load-main-page')

    context = {
        'employee': get_employee,
        'form': form,
        'get_check': get_check
    }

    return render(request, 'employees/focused-employee.html', context)

