from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from django.db.models import Q,Count,Sum
from django.views import View
from book.models import Book
from book.forms import BookForm



class BookGroupView(View):
    
    def get(self,request):
        bookObj = Book.objects.values("publish").annotate(count=Sum("booknum"))
        return HttpResponse(bookObj)


class BookListView(View):
    def get(self,request):
        current_page = request.GET.get("page",1)
        search = request.GET.get("search","")
        bookObj = Book.objects
        if search:
            bookObj = bookObj.filter(Q(bookname__contains=search) | Q(writer__contains=search) | Q(publish__contains=search))
        else:
            bookObj = bookObj.all()
        
        pageObj = Paginator(bookObj,2)
        page = pageObj.page(current_page)
        dataList = page.object_list
        return render(request,"book/listBook.html",{
            "dataList":dataList,
            "page":page,
            "current_page" : int(current_page),
            "page_range" : pageObj.page_range,
            "search" : search
            })
    
class BookView(View):
    
    def get(self,request):
        f = BookForm()
        return render(request,"book/addBook.html",{"form":f})
    
    def post(self,request):
        f = BookForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect("book:listBook")
        else:
            return render(request,"book/addBook.html",{"form":f})
        
class BookUpdateView(View):
    
    def get(self,request,id):
        BookObj = Book.objects.get(id=id)
        f = BookForm(instance=BookObj)
        return render(request,"book/updateBook.html",{"form":f})
    
    def post(self,request,id):
        BookObj = Book.objects.get(id=id)
        f = BookForm(instance=BookObj,data=request.POST)
        if f.is_valid():
            f.save()
            return redirect("book:listBook")
        else:
            return render(request,"book/addBook.html",{"form":f})
        
class BookDeleteView(View):
    def get(self,request,id):
        BookObj = Book.objects.get(id=id).delete()
        return redirect("book:listBook")