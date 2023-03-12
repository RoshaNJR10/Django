from django.shortcuts import render, HttpResponse
from .models import student

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