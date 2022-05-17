from django.db import models

# Create your models here.


class User(models.Model):
    
    username = models.CharField(max_length=32,verbose_name="用户名")
    passwd = models.CharField(max_length=64,verbose_name="密码")
    
    
class Book(models.Model):
    
    bookname = models.CharField(max_length=32,verbose_name="图书名称")
    booknum = models.SmallIntegerField(verbose_name="图书数量")
    publish = models.CharField(max_length=32,verbose_name="出版社")
    writer = models.CharField(max_length=32,verbose_name="作者")
    status_choice = (
        (0,"未上架"),
        (1,"已上架")
    )
    status = models.SmallIntegerField(choices=status_choice,verbose_name="状态")
    pubdate = models.DateTimeField(verbose_name="出版日期")
    

class Colleges(models.Model):
    name = models.CharField(max_length=32,verbose_name="系名称")
    
    def __str__(self):
        return self.name
    
class Grade(models.Model):
    name = models.CharField(max_length=32,verbose_name="班级名称")
    college = models.ForeignKey(to="Colleges",on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.name
    
class Student(models.Model):
    name = models.CharField(max_length=32,verbose_name="姓名")
    passwd = models.CharField(max_length=32,verbose_name="密码")
    stunum = models.CharField(max_length=32,verbose_name="学号")
    college = models.ForeignKey(to="colleges",on_delete=models.DO_NOTHING)
    grade = models.ForeignKey(to="Grade",on_delete=models.DO_NOTHING)
    lendnum = models.SmallIntegerField(null=True,blank=True,default=0,verbose_name="借阅数量")
    phone = models.CharField(max_length=11,verbose_name="手机号")
    email = models.EmailField(verbose_name="邮箱")
    stu_choice = (
        (0,"已毕业"),
        (1,"未毕业")
    )
    status = models.SmallIntegerField(choices=stu_choice,verbose_name="在校状态")
    login_datetime = models.DateTimeField(null=True,blank=True)
    create_time = models.DateTimeField(auto_now_add=True) 
    
    
    def __str__(self):
        return self.name

    

    
    