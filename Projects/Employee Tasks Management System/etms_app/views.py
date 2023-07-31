from django.shortcuts import render
from .models import Employee, Task

# Create your views here.
def home(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def dashboard(request):
    user = request.user
    if user.is_superuser:
        print("You are an admin")
        employees = Employee.objects.all()
        tasks = Task.objects.all()
        completed = Task.objects.filter(doc__isnull=False)
        pending = Task.objects.filter(doc__isnull=True)

        context = {
            'emps': employees,
            'tasks': tasks,
            'completed': completed,
            'pending': pending
        }

    else: 
        employee = user.employee
        tasks = Task.objects.filter(employee=employee) 

        context = {
            'emp': employee,
            'tasks': tasks,
        }
        
        print("You are an employee")
    return render(request, 'index.html', context)

def employees(request):
    return render(request, 'docs.html')

def tasks(request):
    return render(request, 'orders.html')