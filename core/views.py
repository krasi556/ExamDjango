from django.shortcuts import render, redirect

from employees.models import Employee


# Create your views here.

def load_main_page(request):
    top_employee = Employee.objects.get_top_rated()

    context = {
        'employee': top_employee
    }
    return render(request, 'core/main-page.html', context)


def handle_error404(request, exception):
    return render(request, '404.html', status=404)


def redirect_to_main_page(request):
    return redirect('core:load-main-page')
