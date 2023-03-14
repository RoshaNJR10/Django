from django.shortcuts import render, HttpResponse,redirect
from django.contrib import admin
from .models import student
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages
from django.core.mail import send_mail



# Create your views here.
def function(request):
    data=student.objects.all()
    d={
        "data":data
    }
    if request.method=='POST':
        name=request.POST['name'];
        add=request.POST['address'];
        roll=request.POST['roll'];
        contact=request.POST['contact'];
        # gen=request.POST['gender'];
        # fac=request.POST['faculty'];
        # user=request.POST['email'];
        # pas=request.POST['pass'];
        stdinfo=student(name=name,address=add,roll=roll,contact=contact)
        stdinfo.save()
       
        print(name, add,roll,contact)
        # d={
        #     'name':name,
        #     'address':add,
        #     'gender':gen,
        #     'faculty':fac,
        #     'username':user,
        #     'password':pas,
            
        #     'roll':roll,
        #     'contact':contact,

        # }
        return render(request,'table.html',d)
    return render(request, 'index.html')

def signup(request):
    if request.method=='POST':
        username=request.POST['name']
        email=request.POST['email']
        pas=request.POST['pass']
        user=User(
            username=username,
            email=email,
            password=pas
        )
        user.save()
        messages.success(request, 'User created successfully!!!')
        return redirect('signup')
    return render(request,'signup.html')

def login(request):
    if request.method=='POST':
        username=request.POST['name']
        pas=request.POST['pass']
       
        user=authenticate(request, username=username, password=pas)
        print("user=",user)
        if user is not None:
            print("abc")
            return redirect('home')
        else:
            print("eee")
            messages.info(request, "username or password incorrect")
            return redirect('login')
    return render(request, 'login.html')
def email(request):
    if request.method=='POST':
        to=request.POST['to']
        cc=request.POST['cc']
        sub=request.POST['subject']
        mes=request.POST['message']

        send_mail(
            sub,
            mes,
            'adhikariroshan042@gmail.com',
            [to,cc],
            fail_silently=False
        
        )
        messages.success(request, 'Email send Successfully!!!')
        return redirect('email')
    return render(request, 'mail.html')