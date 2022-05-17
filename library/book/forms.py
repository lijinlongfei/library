from django import forms
from book.models import User,Book,Colleges,Grade,Student


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
        widgets = {
            "username" : forms.TextInput(attrs={"class":"form-control"}),
            "passwd" : forms.PasswordInput(attrs={"class" : "form-control"})
        }
        
        
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
        widgets = {
            "bookname" : forms.TextInput(attrs={"class":"form-control"}),
            "publish" : forms.TextInput(attrs={"class":"form-control"}),
            "writer" : forms.TextInput(attrs={"class":"form-control"}),
            "status" : forms.Select(attrs={"class":"form-control"}),
            "pubdate" :forms.TextInput(attrs={"class":"form-control"}),
        }
        
        
class CollegesForm(forms.ModelForm):
    class Meta:
        model = Colleges
        fields = "__all__"
        
        
class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = "__all__"
        
        
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ["lendnum","login_datetime","create_time"] 
        