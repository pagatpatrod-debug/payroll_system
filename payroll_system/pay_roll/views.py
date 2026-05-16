from django.shortcuts import render, redirect
from .models import Employee, Payroll

def login_view(request):
    if request.method == 'POST':
        return redirect('dashboard')
    return render(request, 'log_in.html')

def dashboard(request):
    return render(request, 'dashboard.html', {
        'employee_count': Employee.objects.count(),
        'payroll_count': Payroll.objects.count(),
    })

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {
        'employees': employees
    })

def payroll_list(request):
    payrolls = Payroll.objects.all()
    return render(request, 'payroll_list.html', {
        'payrolls': payrolls
    })