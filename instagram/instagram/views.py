from django.http import HttpResponse
from django.shortcuts import render

# def homepage(request):
#     return HttpResponse('Welcome to Backend with django')
def notfound(request):
    return render(request, "404.html")