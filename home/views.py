from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    peoples=[
        {'name' : 'Abhijeet Gupta','age':23},
        {'name' : 'Abhishek Gupta','age':22},
        {'name' : 'Abhi Gupta','age':29},
        {'name' : 'vishwajeet Gupta','age':13},

    ]
   


    return render(request,"home/index.html",context={'peoples':peoples})


def success_page(request):
    return HttpResponse("this is a success page")

def about(request):
    return render(request,"home/about.html")

def contact(request):
    context={'page' : 'Contact'}
    return render(request,"home/contact.html",context)
