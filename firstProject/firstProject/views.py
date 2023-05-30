from django.http import HttpResponse
from django.shortcuts import render

# Functionalities

# functions

# def index -> Display home page 
# def index(request):
#     return HttpResponse("<h1>This is the home page of my website.</h1><p>This is my first time learning Djanlwhfkaer kaf kaeraertfkaeu r</p>")

def index(request):
    return render(request, 'index.html') 

# def about(request):
#     return HttpResponse("This is the 'ABOUT US' page of my website")

def about(request):
    return render(request, 'aboutUs.html')

def team_section(request):
    return HttpResponse("This is where I'll be showing all about my team")
# process incoming Request -> Generate response (HttpResponse)
# M V T
# def about -> Display about us page
# Static files -> HTML | CSS | JS | Images(Static files)


# JS - CSS (Internal | External)