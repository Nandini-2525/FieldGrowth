from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse("Hello from fieldgrowth")
def home(request):
    return render(request,"index.html")