from django.shortcuts import render
from .forms import LoginForm, EmployeeForm

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)      # bound form
        # print(form)
        if form.is_valid():
            # cleanse the data and creates a separate collection of that 
            print(form.cleaned_data)
        else:
            print(form.errors)

            # you save the that collection into the database if required

    form = LoginForm()      # unbound form
    # print(form)
    return render(request, 'app1/home.html', {'form': form, })

def intro(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)

        if form.is_valid(): 
            # save the data in database
            form.save()

    form = EmployeeForm()
    return render(request, 'app1/intro.html', {'form': form, })
