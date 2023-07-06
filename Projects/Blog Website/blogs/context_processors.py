# Define functions that return dictionary. The keys of this dictionary will be accessible in the application globally.
from .models import Blog, Category

def blogs_and_categories(request):
    all_blogs = Blog.objects.all()
    all_categories = Category.objects.all()
    return {'all_blogs':all_blogs, 'all_categories':all_categories}