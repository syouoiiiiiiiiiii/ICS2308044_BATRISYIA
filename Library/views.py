from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Student
from .models import Book
from .models import Borrowing
from .models import Course
from .models import Mentor
# Create your views here.
def view(request):
    context = {
        'lastname' : 'BATRISYIA'
    }
    return render (request,"view.html",context)

def index(request):
    context = {
        'greeting' : 3,

    }
    return render (request,"index.html",context)

def dbstudent(request):
    mystudent = Student.objects.all().values()
    context = {
        'mystudent' : mystudent,
    }
    return render (request,"dbstudent.html",context)

def dbbook(request):
    mybook = Book.objects.all().values()
    context = {
        'mybook' : mybook,
    }
    return render (request,"dbbook.html",context)

def dbborrow(request):
    myborrow = Borrowing.objects.all().values()
    context = {
        'myborrow' : myborrow,
    }
    return render (request,"dbborrow.html",context)

def course(request):
    mycourse = Course.objects.all()

    if request.method == 'POST':
        c_code = request.POST['code']
        c_desc = request.POST['description']
        
        data = Course(code=c_code, description=c_desc)
        data.save()
        
    context = {
        'mycourse': mycourse,
        'message': ''  
    }
    
    return render(request, "course.html", context)

def newmentor(request):
    if request.method == 'POST':
        m_id = request.POST['menid']
        m_name = request.POST['menname']
        m_roomno = request.POST['menroomno']
        
        data = Mentor(menid=m_id, menname=m_name, menroomno=m_roomno)
        data.save()
        
        mymentor = Mentor.objects.all().values()
        
        dict = {
            'message': 'Data Saved',
            'mymentor': mymentor,  
        }
    else:
       
        mymentor = Mentor.objects.all().values()
        dict = {
            'message': '',
            'mymentor': mymentor,
        }
        
    return render(request, 'newmentor.html', dict)

def update_course(request, code): 
    course = Course.objects.get(code=code)
    mycourse = Course.objects.all()  
    context = {
        'course': course,
        'mycourse': mycourse
    }
    return render(request, "update_course.html", context)

def save_update_course(request, code):
    c_desc = request.POST['description']
    course = Course.objects.get(code=code)
    course.description = c_desc
    course.save()
    
    return HttpResponseRedirect(reverse("Course"))

def delete_course(request, code):
    course = Course.objects.get(code = code)
    course.delete()
    return HttpResponseRedirect(request,reverse("Course"))

def update_newmentor(request, menid): 
    x = Mentor.objects.get(menid = menid)
    mymentor = Mentor.objects.all()  
    context = {
        'x': x,
        'mymentor': mymentor
    }
    return render(request, "update_newmentor.html", context)

def save_update_newmentor(request, menid):
    m_name = request.POST['menname']
    m_roomno = request.POST['menroomno']
    x = Mentor.objects.get(menid = menid)
    x.menname = m_name
    x.menroomno = m_roomno
    x.save()
    return HttpResponseRedirect(reverse("Mentor"))

def delete_newmentor(request, menid):
    x = Mentor.objects.get(menid=menid)
    x.delete()
    return HttpResponseRedirect(reverse("Mentor"))

def search_course(request):
    if request.method == 'GET':
        c_code=request.GET.get('c_code')

        if c_code:
            mycourse = Course.objects.filter(code=c_code.upper())
        else:
            mycourse = None

        context = {
            'mycourse' : mycourse
        }
        return render(request, "search_course.html", context)
    return render(request, "search_course.html")

def search_mentor(request):
    if request.method == 'GET':
        m_id=request.GET.get('m_id')

        if m_id:
            mymentor = Mentor.objects.filter(menid=m_id.upper())
        else:
            mymentor = None
        context = {
            'mymentor' : mymentor
        }
        return render(request, "search_mentor.html", context)
    return render(request, "search_mentor.html")