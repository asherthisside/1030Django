from django.shortcuts import render, redirect
from .models import Employee, Task
from datetime import datetime

# Create your views here.
def home(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def dashboard(request):
    user = request.user
    # completed = Task.objects.filter(doc__isnull=False)
    # pending = Task.objects.filter(doc__isnull=True)
    employee = user.employee
    pending_tasks = Task.objects.filter(employee=employee, doc__isnull=True) 
    completed_tasks = Task.objects.filter(employee=employee, doc__isnull=False) 

    context = {
        'emp': employee,
        'completed': completed_tasks,
        'pending': pending_tasks,
    }
    
    return render(request, 'emp_dash.html', context)

def mark_as_completed(request, id):
    task = Task.objects.get(id=id)
    task.doc = datetime.now()
    task.save()
    print(task)
    return redirect("/dashboard")