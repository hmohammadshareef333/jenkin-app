from django.shortcuts import render,redirect
from .models import studentform
from django.db.models import Q
# Create your views here.
def home(request):
    data=studentform.objects.all()
    print(data)
    if 'query' in request.GET:
        var=request.GET['query']
        data=studentform.objects.filter(Q(ename__icontains=var)|Q(rollno__icontains=var)|Q(course__icontains=var))
    return render(request,'home.html',{'record':data})
def add(request):
    c=None
    if request.method=='POST':
        ename1=request.POST['ename']
        rollno1=request.POST['rollno']
        course1=request.POST['course']
        mobileno1=request.POST['mobileno']
        img2=request.POST['image']
        c=studentform.objects.create(ename=ename1,rollno=rollno1,course=course1,mobileno=mobileno1,image=img2)
        print(c)
        return redirect('home')
    
    return render(request,'add.html',{'data':c})
def editning(request,id):
    data=studentform.objects.get(id=id)
    if request.method == 'POST':
        studentname_edit=request.POST['ename']
        Rollnumber_edit=request.POST['rollno']
        Course_edit=request.POST['course']
        mobilenumber_edit=request.POST['mobileno']
        print(studentname_edit,Rollnumber_edit,Course_edit,mobilenumber_edit)
        data.ename=studentname_edit
        data.rollno=Rollnumber_edit
        data.course=Course_edit
        data.mobileno=mobilenumber_edit
        data.save()
        return redirect('home')
    return render(request,'edit.html',{'record':data})
def dele(request,id):
        a=studentform.objects.get(id=id)
        a.delete()
        return redirect('home')
def history(request):
    return render(request,'history.html')