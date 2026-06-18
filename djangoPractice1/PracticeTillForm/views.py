from django.shortcuts import render
from .forms import ContactForm
# Create your views here.
def home(request):
    makeform=ContactForm()
    data={'form':makeform}
    return render(request,'practiceForm/home.html',data)

