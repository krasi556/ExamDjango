from django.shortcuts import render, redirect


# Create your views here.

def load_main_page(request):
    return render(request, 'core/main-page.html', )


def handle_error404(request, exception):
    return render(request, '404.html', status=404)


def redirect_to_main_page(request):
    return redirect('core:load-main-page')
