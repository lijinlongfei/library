from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views import View
from book.models import Colleges,Grade
from book.forms import CollegesForm,GradeForm


class CollegeView(View):
    
    def get(self,request):
        f = CollegesForm()
        return render(request,"book/addCollege.html",{"form":f})
    
    
    def post(self,request):
        f = CollegesForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect("book:listCollege")
        else:
            return render(request,"book/addCollege.html",{"form":f})
    
class CollegeListView(View):
    
    def get(self,request):
        collObj = Colleges.objects.all()
        return render(request,"book/listCollege.html",{"dataList":collObj})





class GradeView(View):
    
    def get(self,request):
        
        f = GradeForm()
        return render(request,"book/addGrade.html",{"form":f})
    
    
    def post(self,request):
        f = GradeForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect("book:listGrade")
        else:
            return render(request,"book/addGrade.html",{"form":f})
    
class GradeListView(View):
    
    def get(self,request):
        collObj = Grade.objects.all()
        return render(request,"book/listGrade.html",{"dataList":collObj})

