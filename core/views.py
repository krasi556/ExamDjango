from django.shortcuts import render

# Create your views here.

def load_main_page(request):
    return render(request,'core/main-page.html',)