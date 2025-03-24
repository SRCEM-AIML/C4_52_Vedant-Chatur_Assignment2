from django.shortcuts import render

def home(request):
    return render(request, 'app1/index.html')

def sample1(request):
    return render(request, 'app1/sample1.html')
