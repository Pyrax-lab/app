from django.http import HttpResponse
from django.shortcuts import render

def index(request):

    context = {
    "title": "HomePage",
    "about": "Thisis a simple page on Django"
    "isinstance: False"}

    return render(request, "main/index.html", context)

def about(request):
    
    return HttpResponse("About page nigga")