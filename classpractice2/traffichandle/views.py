from django.shortcuts import render
from .forms import trafficForm

def home(request):
    trafficform=trafficForm()
    data = {
        'form':trafficform
    }
    return render(request,'traffic/home.html',data)
def displaydata(request):
    data1 = int(request.POST.get("timePeriod"))
    data = {
        'firstfield':data1
    }
    if(data1>5):
        return render(request,'traffic/error.html',data)
    return render(request,'traffic/display.html',data)
# Create your views here.
def error(request):
    return render(request,'traffic/error.html')
