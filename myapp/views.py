from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def helllo(request):
    return HttpResponse("<h2>Hello World</h2>")

def about(request):
    return HttpResponse("<h2>About Page</h2>")