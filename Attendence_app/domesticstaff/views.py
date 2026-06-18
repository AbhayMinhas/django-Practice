from django.shortcuts import render
from .forms import attendencemark
import datetime
# Create your views here.
data_of_employees={'employee1':10,
                   'employee2':20,
                   'employee3':30}
employees_present={}
def attendenceForm(request):
    attendace_func=attendencemark()
    data1={
        'data':attendace_func,
    }
    return render(request,'attendence/home.html',data1)
def Mark(request):
    regestration = int(request.POST.get("reg_no"))
    ispresent = bool(request.POST.get("ismarked"))
    reg_list=list(data_of_employees.values())
    flag=False
    for reg in reg_list:
        if(reg==regestration):
            flag=True
    if(flag==False):
        data1={'data':'Person not in database'}
        return render(request,'attendence/result.html',data1)
    if(ispresent==True):
        employees_present[datetime.datetime.now()]=regestration
        data1={'data':'attendence is marked present'}
        return render(request,'attendence/result.html',data1)
    data1={'data':'abscent'}
    return render(request,'attendence/result.html',data1)