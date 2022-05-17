from django.urls import path
from book.views.login import LoginView,LogoutView
from book.views.book import BookView,BookListView,BookUpdateView,BookDeleteView,BookGroupView
from book.views.college import CollegeView,CollegeListView,GradeListView,GradeView
app_name = "book"

urlpatterns = [
    path(r"login/",LoginView.as_view(),name="login"),
     path(r"logout/",LogoutView.as_view(),name="logout"),
    
    path(r"bookList/",BookListView.as_view(),name="listBook"),
    path(r"bookAdd/",BookView.as_view(),name="addBook"),
    path(r"bookUpdate/<int:id>/",BookUpdateView.as_view(),name="updateBook"),
    path(r"bookDelete/<int:id>/",BookDeleteView.as_view(),name="deleteBook"),
    path(r"bookGroup/",BookGroupView.as_view(),name="groupBook"),
    
    path(r"collegeAdd/",CollegeView.as_view(),name="addCollege"),
    path(r"collegeList/",CollegeListView.as_view(),name="listCollege"),
    
    path(r"gradeAdd/",GradeView.as_view(),name="addGrade"),
    path(r"gradeList/",GradeListView.as_view(),name="listGrade"),
]
