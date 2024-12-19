from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def login_user(request):
    return render(request, 'admin_dashboard/login_user.html')

def redef_senha(request):
    return render(request, 'admin_dashboard/redef_senha.html')

def senha(request):
    return render(request, 'admin_dashboard/senha.html')

# @login_required
def index(request):
    return render(request, 'admin_dashboard/index.html')

def relatorio(request):
    return render(request, 'admin_dashboard/relatorio.html')

def eventos(request):
    return render(request, 'admin_dashboard/eventos.html')

def turmas(request):
    return render(request, 'admin_dashboard/turmas.html')
