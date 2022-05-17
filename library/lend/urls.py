from django.urls import path
from lend.views.student import StudentView,StudentListView


app_name = "lend"
urlpatterns = [
   path(r"addStudent/",StudentView.as_view(),name="addStudent"),
   path(r"listStudent/",StudentListView.as_view(),name="listStudent"),
]
