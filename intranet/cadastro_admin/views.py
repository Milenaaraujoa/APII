from django.contrib.auth.decorators import login_required
from django.shortcuts import render

def login_user(request):
    return render(request, 'admin_dashboard/login_user.html')

@login_required
def index(request):
    return render(request, 'admin_dashboard/index.html')
