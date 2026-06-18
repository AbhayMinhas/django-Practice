from django.shortcuts import render
from .forms import userform
from .models import genderdetails
def home(request):
    user=userform()
    if(request.method=='POST' and request.POST.get('delete')=='delete'):
        name1=request.POST.get('name')
        gender1=genderdetails.objects.filter(name=name1).first()
        gender1.gender="Female"
        gender1.save()
        return render(request,'prac/home.html',{'delete':'data deleted sucessfully','userform':user})
        
    context={
        'userform':user,
        'title':'home',
    }
    return render(request,'prac/home.html',context)
# Create your views here.
def res(request):
    name1=request.POST.get('name')
    gender1=request.POST.get('gender')
    details=genderdetails(name=name1,gender=gender1)
    details.save()
    context={'name':name1,'gender':gender1}
    return render(request,'prac/res.html',context)
