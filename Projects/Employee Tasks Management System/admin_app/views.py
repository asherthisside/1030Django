from django.shortcuts import render
from etms_app.models import Task, Employee

# Create your views here.

def dashboard(request):
    emps = Employee.objects.all().count()
    pending_tasks = Task.objects.filter(doc__isnull=True).count()
    completed_tasks = Task.objects.filter(doc__isnull=False).count()

    context = {
        'emp': emps,
        'completed': completed_tasks,
        'pending': pending_tasks,
    }
    return render(request, 'admin_dash.html', context)

def employees(request):
    return render(request, 'employees.html')

def tasks(request):
    pending_tasks = Task.objects.filter(doc__isnull=True) 
    completed_tasks = Task.objects.filter(doc__isnull=False) 

    context = {
        'completed': completed_tasks,
        'pending': pending_tasks,
    }
    return render(request, 'tasks.html', context)