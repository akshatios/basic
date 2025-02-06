from django.core import paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import UserForm
from service.models import Service
from news.models import News
from django.core.paginator import Paginator

def Homepage(request):
    newsData=News.objects.all();
    
    ServicesData=Service.objects.all()
    for a in ServicesData:
        print(a.service_icon)
        print(a.service_title)
    print(Services)
    
    data = {
         'servicesData':ServicesData,
        
        'title':'Home New',
        'h1':'Welcome to Our Django Website Home Page',
        'clist':["PHP","python","java"],
        "student_details":[
            {"Name":"Akshat","Phone":91033214222},
            {"Name":"abhisehk","Phone":56783241990},
        ]
    }
    return render(request,"index.html",data)


def aboutUs(request):
    
    if request.method=='GET':
        output=request.GET.get('output')
    return render(request,"about.html",{"output":output})


def Services(request):
    ServicesData = Service.objects.all()
    
    paginator=Paginator(ServicesData,2)
    page_number=request.GET.get('page')
    ServiceDatafinal=paginator.get_page(page_number)
    
    
    if request.method=="GET":
        st=request.GET.get('servicename')
        if st!=None:
            ServicesData = Service.objects.filter(service_title__icontains=st)

    data = {'servicesData': ServicesData}
    return render(request, "services.html", data)

  
def calculator(request):
    
    c=''
    try:
        if request.method=='POST':
            n1=eval(request.POST.get('num1'))
            n2=eval(request.POST.get('num2'))
            opr=request.POST.get('opr')
            if opr=="+":
                c=n1+n2
            elif opr=="-":
                c=n1-n2
            elif opr=="*":
                c=n1*n2
            elif opr=="/":
                c=n1/n2
    except:
        c="Invalid opr...."
    print(c)      
    return render(request,"calculator.html",{'c':c})


def contact(request):
    return render(request,"contact.html")


def course(reuqest):
    return HttpResponse("wellcome to course page")

 
def CourseDetails(reuqest,courseid):
    return HttpResponse(courseid)


def userform(request):
    finalans= ''
    fn=UserForm()
    
    data={'form':fn}
    
    try:
        if request.method=="POST":
            n1 = request.POST.get('name')
            n2 = request.POST.get('email')
            n3 = request.POST.get('gender')
            n4 = request.POST.get('country')

            
            finalans = f"Name: {n1}, Email: {n2}, Gender: {n3}, Country: {n4}"
            data={
                'form':fn,
                'output':finalans
            }
            
            url="/about-us/?output={}".format(finalans)
            
            return HttpResponseRedirect(url)
            
    except Exception as e:
        print(f"error occurred: {e}")
        
    return render(request,"userform.html",{'output':finalans})

