from django.shortcuts import redirect,render
from django.views import View
from book.models import Grade,Colleges,Student
from book.forms import StudentForm


class StudentView(View):
    
    def get(self,request):
        f = StudentForm()
        return render(request,"lend/addStudent.html",{"form":f})
    
    def post(self,request):
        f = StudentForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect("lend:listStudent")
        else:
            return render(request,"lend/addStudent.html",{"form":f})


class StudentListView(View):
    
    def get(self,request):
        searchCollege = request.GET.get("searchCollege",'')
        searchGrade = request.GET.get("searchGrade","")
        searchName = request.GET.get("searchName","")
        
        stuObj = Student.objects.all()
        if searchCollege:
            stuObj = stuObj.filter(college__name__contains=searchCollege)
        if searchGrade:
            stuObj = stuObj.filter(grade__name__contains=searchGrade)
        if searchName:
            stuObj = stuObj.filter(name__contains=searchName)
        
        return render(request,"lend/listStudent.html",{"dataList":stuObj})