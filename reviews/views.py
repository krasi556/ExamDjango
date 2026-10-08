from django.db.models import Avg
from django.db.transaction import commit
from django.shortcuts import render, get_object_or_404, redirect

from employees.forms import CreateEmployee, EditEmployee
from employees.models import Employee
from reviews.forms import ReviewForms, CreateReview, EditReview, DeleteReview
from reviews.models import Review


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
    return render(request, 'reviews/review-details.html', context)


def current_employee_reviews(request, employee_id):
    get_employee = get_object_or_404(
        Employee.objects
        .annotate(avg_rating=Avg('reviews__rating'))
        .prefetch_related('reviews'),
        id=employee_id)
    if request.method == 'POST':
        form = ReviewForms(request.POST)
        pass

    context = {
        'employee': get_employee,
        'reviews': get_employee.reviews.all()
    }

    return render(request, 'reviews/show-reviews-for-current-employee.html', context)


def edit_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    form = EditReview(request.POST or None, instance=review)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('employees:focused-employee', employee_id=review.employee_id)
    context = {
        'form': form,
        'employee': review.employee,
        'review': review
    }
    return render(request, 'reviews/edit-review.html', context)


def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    form = DeleteReview(request.POST or None, instance=review)
    if form.is_valid() and form.is_valid():
        review.delete()
        return redirect('reviews:current-employee-reviews', review.employee_id)
    context = {
        'form': form,
        'review': review,
        'employee': review.employee,
    }
    return render(request, 'reviews/delete-review.html', context)
