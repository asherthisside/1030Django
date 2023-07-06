from django.shortcuts import render, redirect
from .models import Category, Blog, Author
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib import auth
# Create your views here.

@login_required(login_url='/login')
def index(request):
    return render(request, 'index.html')

@login_required(login_url='/login')
def single(request, id):
    blog = Blog.objects.get(id=id)
    context = {
        'blog': blog
        }
    return render(request, 'blog-single.html', context)

def signup(request):
    # request POST 
    if request.method == 'POST':
        # Data collect from the form
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        uname = request.POST['uname']
        pswd1 = request.POST['password1']
        pswd2 = request.POST['password2']

        # validations 
            # Password should match 
        if pswd1 == pswd2:
            # Username should be unique 
            if User.objects.filter(username=uname).exists():
                # send a message that username already exists
                messages.error(request, "Username already exists")
                # Redirect to same page
                return redirect("/signup")
            
            elif User.objects.filter(email=email).exists():
                # Send a message that email is already in use
                messages.error(request, "Email is already in use")
                # Redirect to same page
                return redirect("/signup")
            
            else: 
                User.objects.create_user(first_name=fname, last_name=lname, email=email, username=uname, password=pswd1)
                # Success message: Sign up successful
                messages.success(request, "Account Created successfully")

                # redirect to login page 
                return redirect("/login")

            # Mail ID should not be in use 

            # Create User 

        else:
            # Message: Password not matching   
            messages.error(request, "Passwords do not match") 
            # Redirect to same page 
            return redirect("/signup")

    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        # Data collect from the form 
        uname = request.POST['uname']
        pswd= request.POST['password']

        # Authenticate the user whether it exists or not 
        user = auth.authenticate(request, username=uname, password=pswd)

        if user is not None:
            auth.login(request, user=user)
            messages.success(request, "Log in successful")
            return redirect("/")
        else:
            messages.error(request, "Invalid credentials. Please try again.")
            return redirect("/login")
    else:
        return render(request, 'login.html')
    
def logout(request):
    messages.success(request, "Logged out Successfully")
    auth.logout(request)
    return redirect("/login")

def author_reg(request):
    if request.method == 'POST':
        # Fetch the category selected by user
        user_cat = request.POST['category']
        category = Category.objects.get(name=user_cat)

        # create author object -> category (from form) | User (request.user)
        new_author = Author(category=category, user=request.user)
        new_author.save()

        messages.success(request, "You have successfully registered as Author. Go to Dashboard for further details")

        return redirect("/")
    return render(request, 'author_reg.html')

def author_dashboard(request):
    blogs = Blog.objects.filter(author=request.user.author)
    return render(request, 'author_dashboard.html', {'blogs':blogs})

def author_add_blog(request):
    if request.method == 'POST':

        # values fetch 
        title = request.POST['title']
        description = request.POST['description']
        category = request.POST['category']
        cat = Category.objects.get(name=category)
        image = request.FILES['image']

        print(title, description, category, image)

        # Create a blog object 
        new_blog = Blog(title=title, description=description, category=cat, author=request.user.author, image=image)

        # save the object
        new_blog.save()

        return redirect("/author_dashboard")
    return render(request, 'author_add_blog.html')

def author_update_blog(request, pk):
    # fetch the object that needs to be edited
    blog = Blog.objects.get(id=pk)

    if request.method == 'POST':
        # values fetch 
        title = request.POST['title']
        description = request.POST['description']

        # values overwrite
        blog.title = title
        blog.description = description

        # save the object
        blog.save()

        # redirect to dashboard
        return redirect('/author_dashboard')
    return render(request, 'author_update_blog.html', {'blog':blog})

def author_delete_blog(request, pk):
    # fetch the blog
    blog = Blog.objects.get(id=pk)
    
    # delete the blog 
    blog.delete()

    # redirect to the dashboard
    return redirect('/author_dashboard')

def category_wise(request, name):
    # fetch blogs where category matches
    category = Category.objects.get(name=name)
    blogs = Blog.objects.filter(category=category)
    
    # fill the context with these blogs
    context = {'blogs':blogs, 'category':category}

    # render the page in that context
    return render(request, 'category_wise.html', context)

# Context: 

# Context processors: functions that return a dictionary