from django.shortcuts import render
from .forms import potform
# Create your views here.

def home(request):
    tree=request.COOKIES.get('tree')
    pot=request.COOKIES.get('pot')
    if(request.POST.get('pot')):
        pot=request.POST.get('pot')
        context={
        'tree':tree,
        'pot':pot,
        }
        response=render(request,'plant/home.html',context)
        response.set_cookie('pot',pot)
        return response
    else:
        context={
        'tree':tree,
        'pot':pot
                 }
        return render(request,'plant/home.html',context)

def pot(request):
    tree=request.POST.get('tree')
    pot1=potform()
    context={'tree':tree,'pot':pot1}
    response=render(request,'plant/pot.html',context)
    response.set_cookie('tree',tree)
    return response
