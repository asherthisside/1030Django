from django.shortcuts import render, redirect
from .models import Employee

# Create your views here.
def explore(request):
    # Use Manager object of Employee Model
    # Fetch all the data 
    employees = Employee.objects.all()           # Returns a manager object
    # SELECT * FROM `employees`
    # SELECT * FROM `employees` WHERE `id` = 1
    # print(employees)
    # Fill that data in the context

    context = {
        'employees': employees,
    }

    # Render the template with that context
    return render(request, 'app2/explore.html', context)

def show_reels(request):
    return render(request, 'app2/show_reel.html')

def add_employee(request):
    if request.method == 'POST': 
        # fetch form data 
        entered_name = request.POST['name']
        entered_deptt = request.POST['deptt']
        entered_salary = request.POST['salary']

        # save in database 
            # create an Employee object 
        # emp = Employee(name=entered_name, deptt=entered_deptt, salary=entered_salary)
        # Save in database
        # emp.save()
        
        Employee.objects.create(name=entered_name, deptt=entered_deptt, salary=entered_salary)


        return redirect("/two")

    else:
        return render(request, 'app2/add_employee.html')

def update(request, pk):
    emp = Employee.objects.get(id=pk)
    if request.method == "POST":
        # Data fetch from form
        entered_name = request.POST['name']
        entered_deptt = request.POST['deptt']
        entered_salary = request.POST['salary']
         
        # Properties of model object will be overridden 
        emp.name = entered_name
        emp.deptt = entered_deptt
        emp.salary = entered_salary

        # Save the object
        emp.save()

        # Redirect to main page
        return redirect("/two")

    else:
        return render(request, 'app2/update.html', {'emp':emp, 'pk':pk})
    
def delete(request, pk):
    # Get employee object by its ID 
    employee = Employee.objects.get(id=pk)

    # Delete object
    employee.delete()

    # Redirect to main page
    return redirect("/two")
