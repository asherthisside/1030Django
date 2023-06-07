from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'app1/home.html')

def intro(request):
    return render(request, 'app1/intro.html')
