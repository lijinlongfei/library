from django.shortcuts import render,redirect
from book.forms import UserForm
from django.views import View
from book.models import User


class LoginView(View):
    
    def get(self,request):
        f = UserForm()
        return render(request,"book/login.html",{"form":f})
    
    def post(self,request):
        f = UserForm(request.POST)
        if f.is_valid():
            userObj = User.objects.filter(
                username = f.cleaned_data["username"],
                passwd = f.cleaned_data["passwd"]
            ).first()
            if userObj:
                request.session["adminLogin"] = {"name":userObj.username}
                request.session.set_expiry(7 * 24 * 3600)
                ret = redirect("book:listBook")
                ret.set_cookie("name",userObj.username,7 * 24 * 3600)
                return ret
            else:
                f.add_error("用户名密码错误")
                return render(request,"book/login.html",{"form":f})
        else:
            return render(request,"book/login.html",{"form":f})
        
class LogoutView(View):
    
    def get(self,request):
        request.session.clear()
        return redirect("book:login")
        



