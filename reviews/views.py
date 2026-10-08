from django.db.transaction import commit
from django.shortcuts import render, get_object_or_404, redirect

from employees.forms import CreateEmployee
from employees.models import Employee
from reviews.forms import ReviewForms, CreateReview


# Create your views here.

def show_employees_for_review(request):
    all_employees = Employee.objects.all()

    form = ReviewForms()
    context = {
        'employees': all_employees,
        'form': form
    }
    return render(request, 'reviews/review-employees.html', context)


def leave_review(request, employee_id):
    employee = get_object_or_404(Employee.objects.prefetch_related('reviews'), id=employee_id)
    form = CreateReview(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            review = form.save(commit=False)
            review.employee = employee
            review.save()
            return redirect('employees:focused-employee', employee_id=employee.id)
    context = {
        'employee': employee,
        'form': form
    }
    return render(request, 'reviews/review-details.html',context)
