from django.shortcuts import render

def home(request):
    intro = "this is initial state of the website"
    return render(request,'home/home.html',{'data':intro});
