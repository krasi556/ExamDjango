from django.core.paginator import Paginator
from django.db.models import Avg, F
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

from django.views.generic import DeleteView, UpdateView, CreateView, DetailView

from core.views import handle_error404
from employees.forms import EmployeeBase, DeleteEmployee, EditEmployee, CreateEmployee, SearchForm, SkillCreate
from employees.models import Employee, Skill
from reviews.forms import ReviewForms
from reviews.models import Review


# Create your views here.

def current_employees(request):
    obj_employees = (Employee.objects
                     .annotate(avg_rating=Avg('reviews__rating'))
                     .order_by(F('avg_rating').desc(nulls_last=True), )
                     )
    paginator = Paginator(obj_employees, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'employees': page_obj
    }
    return render(request, 'employees/employees-in-db.html', context)


class FocusedEmployee(DetailView):
    model = Employee
    template_name = 'employees/focused-employee.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['review_check'] = bool(self.request.GET.get('review_check'))
        # context['review_check'] = False if not self.request.GET.get('review_check') else True

        return context

    def get_queryset(self):
        return (Employee.objects
                .get_avg_rating()
                .prefetch_related('skills')
                )


class LeaveAReview(CreateView):
    model = Review
    form_class = ReviewForms
    success_url = reverse_lazy('employees:current-employees')
    template_name = 'employees/focused-employee.html'

    def find_current_employee(self):
        return get_object_or_404(Employee.objects.get_avg_rating(), pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employee'] = self.find_current_employee()
        context['review_check'] = True
        return context

    def form_valid(self, form):
        form.instance.employee = self.find_current_employee()
        return super().form_valid(form)


class HireEmployee(CreateView):
    model = Employee
    form_class = CreateEmployee
    success_url = 'employees:focused-employee'
    template_name = 'employees/focused-employee.html'

    ## context change

def hire_employee(request, pk):
    if not request.method == 'POST':
        return redirect('employees:focused-employee', pk)
    get_employee = get_object_or_404(Employee, id=pk)
    get_employee.is_available = False
    get_employee.save()
    return redirect('employees:current-employees')


class CreateEmployeeView(CreateView):
    model = Employee
    form_class = CreateEmployee
    success_url = reverse_lazy('employees:new-job')
    template_name = 'employees/create-profile.html'


def new_job(request):
    return render(request, 'employees/redirect-to-new-job.html')


def you_would_miss_out(request):
    return render(request, 'employees/you-miss-out.html')


class EditEmployeeView(UpdateView):
    model = Employee
    template_name = 'employees/edit-employee.html'
    form_class = EditEmployee
    success_url = reverse_lazy('employees:current-employees')


class DeleteEmployeeView(DeleteView):
    model = Employee
    template_name = 'employees/delete-employee.html'
    form_class = DeleteEmployee
    success_url = reverse_lazy('core:load-main-page')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.object
        return kwargs


def show_skills(request):
    get_skills_and_employees = (Skill.objects
                                .prefetch_related('employees'))

    form = SearchForm(request.GET or None)
    skills_checkbox = EmployeeBase()
    employees_with_skills = Employee.objects.filter(skills__isnull=False).distinct().count()
    total_skills = Skill.objects.count()
    if request.method == 'GET' and form.is_valid():
        skill_to_search = form.cleaned_data['search_field']
        try:
            ids = [int(num) for num in request.GET.getlist('skills')]
        except ValueError:
            return handle_error404(request, None)
        if ids:
            get_skills_and_employees = get_skills_and_employees.filter(id__in=ids)
        if skill_to_search:
            get_skills_and_employees = get_skills_and_employees.filter(name__icontains=skill_to_search)
    context = {
        'total_skills': total_skills,
        'skills_and_employees': get_skills_and_employees,
        'form': form,
        'skills_in_checkbox': skills_checkbox,
        'employees_with_skills': employees_with_skills
    }

    return render(request, 'employees/skills/skills-main-menu.html', context)


class AddSkill(CreateView):
    model = Skill
    template_name = 'employees/skills/create-new-skill.html'
    success_url = reverse_lazy('employees:skills-menu')
    form_class = SkillCreate

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['skills'] = Skill.objects.all()
        return context
