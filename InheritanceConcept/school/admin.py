from django.contrib import admin
from .models import ExamCenter,Student,Teacher,Page,Book,Like,Post,Song

# Register your models here.

@admin.register(Song)
class PostAdmin(admin.ModelAdmin):
    list_display = ['song_name','song_duration','sing_by_user']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['post_title','psot_category','post_published','user']



@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['base_id', 'name','roll','cname','city','created_at','updated_at']

@admin.register(Teacher)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','age','city','created_at','updated_at']

@admin.register(Page)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name','date','date','user']

@admin.register(Book)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['book_id','name','auther','pulished_date']

@admin.register(Like)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name','auther','pulished_date','like_name']

