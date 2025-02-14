from django.http import HttpResponse
from django.shortcuts import render
def Home(request):
    return HttpResponse('Hello Gyan Sagar')

def loginpage(request):
    return HttpResponse("welcome in login page")

def logoutpage(request):
    return HttpResponse("welcome in logout page")


def index(request):
    return render(request,'index.html')
from .models import Studentdata
def index(request):
    if request.method=="POST":
        name=request.POST.get('firstname')
        email=request.POST.get('email')
        address=request.POST.get('address')
        temp=Studentdata(Name=name,Email=email,Address=address)
        temp.save()
    return render(request,"index.html")   

from.models import StudentMarks
def Marks(request):
    if request.method=="POST":
        sub1=request.POST.get('sub1')
        sub2=request.POST.get('sub2')
        sub3=request.POST.get('sub3')
        sub4=request.POST.get('sub4')
        sub5=request.POST.get('sub5')
        temp=StudentMarks(sub1=sub1,sub2=sub2,sub3=sub3,sub4=sub4,sub5=sub5)
        temp.save()
    return render(request,'Marks.html')   

# Create your views here.
