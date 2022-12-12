from django.shortcuts import render

# Create your views here.

def show_add(request):
    return render(request, "enroll/show_add.html")

def update(request):
    return render(request, "enroll/update.html")