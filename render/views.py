from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "render/index.html", {})

def next(request):
    return render(request, "render/next.html", {})