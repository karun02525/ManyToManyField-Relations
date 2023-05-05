from django.db import models
from datetime import datetime   
from .managers import CustomManager 
import uuid
from django.contrib.auth.models import User



class Post(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    post_title = models.CharField(max_length=20)
    psot_category = models.CharField(max_length=30)
    post_published = models.DateField()

class Song(models.Model):
    user = models.ManyToManyField(User)
    song_name = models.CharField(max_length=20)
    song_duration = models.IntegerField()
    
    def sing_by_user(self):
        return ",".join([str(i) for i in self.user.all()])




class Page(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE , primary_key=True)
    #user = models.ForeignKey(User,on_delete=models.CASCADE , primary_key=True)
    #user = models.OneToOneField(User,on_delete=models.CASCADE , primary_key=True, limit_choices_to={'is_staff':True})
    #user = models.OneToOneField(User,on_delete=models.PROTECT , primary_key=True)
    name = models.CharField(max_length=30)
    date = models.DateField()



class Book(models.Model):
     book_id = models.IntegerField(primary_key=True)
     name =models.CharField(max_length=20)
     auther = models.OneToOneField(User, on_delete=models.CASCADE)
     pulished_date = models.DateField()
     
class Like(Book):
    like_id=models.OneToOneField(Book,on_delete=Book,primary_key=True,parent_link=True)      
    like_name = models.CharField(max_length=10)
     





class BaseModel(models.Model):
    base_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True


class ExamCenter(BaseModel):
    base_id= None
    cname = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    
class Student(ExamCenter):
    base_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20)
    roll = models.IntegerField()   
    
    
class ProxyStudent(Student):
    str=CustomManager() 
    class Meta:
       proxy=True
       ordering=['name']



class Teacher(BaseModel):
    base_id= None
    teacher_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False),
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    city = models.CharField(max_length=20)
    