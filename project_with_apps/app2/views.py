from django.shortcuts import render

# Create your views here.
def explore(request):
    return render(request, 'app2/explore.html')

def show_reels(request):
    return render(request, 'app2/show_reel.html')