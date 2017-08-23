from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index0(request):
    return HttpResponse("<h1>success</h1>")

def index(request):
    return render(request, "blog/index.html")