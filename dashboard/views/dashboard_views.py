# dashboard/views/dashboard_views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url='login')
def dashboard_view(request):
    try:
        return render(request, 'auth/dashboard.html')
    except Exception as e:
        messages.error(request, f"Dashboard yüklenirken bir hata oluştu: {str(e)}")
        return redirect('login')
