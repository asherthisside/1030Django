from django.shortcuts import render 

def home(request):
    name = "Jyoti"
    city = "Ghaziabad"
    designation = "Business Analyst"
    company = "Infosys"

    context = {
        'name': name, 
        'city': city, 
        'designation': designation, 
        'company': company
        }

    return render(request, 'index.html', context)

def form(request):
    if request.method == 'GET':
        return render(request, 'form.html')

    else:
        # Fetch data from request.POST 
        name = request.POST['username']
        password = request.POST.get('userpass')

        # Fill the data in context 
        context = {
        'name': name,
        'pass': password
        }

        # Render the template with context 
        return render(request, 'form.html', context)

def result(request): 
    # name = request.GET['username']
    # password = request.GET.get('userpass')

    name = request.POST['username']
    password = request.POST.get('userpass')

    # print(request.GET)

    context = {
        'name': name,
        'pass': password
    }

    return render(request, 'result.html', context)


# Total words | Characters | Uppercase chars | Lowercase | Numerals | Special symbols | Alphabets