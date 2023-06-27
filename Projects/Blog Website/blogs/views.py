from django.shortcuts import render
from .models import Category, Blog

# Create your views here.
def index(request):
    categories = Category.objects.all()
    blogs = Blog.objects.all()
    context = {
        'cats': categories, 
        'blogs': blogs
    }
    return render(request, 'index.html', context)

def single(request, id):
    blog = Blog.objects.get(id=id)
    categories = Category.objects.all()
    context = {
        'cats': categories, 
        'blog': blog
        }
    return render(request, 'blog-single.html', context)