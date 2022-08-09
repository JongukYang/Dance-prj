from django.contrib import admin
from .models import Post, Comment, Genre, Course

# Register your models here.

class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(Genre, GenreAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ('userId', 'userId_id', 'title', 'body', 'likes_count', 'genreName', 'uploadDate', 'updateDate')

admin.site.register(Post, PostAdmin)

# 강의
class CourseAdmin(admin.ModelAdmin):
    list_display = ('userId', 'userId_id', 'title', 'body', 'likes_count', 'genreName', 'startDate', 'uploadDate', 'updateDate')

admin.site.register(Course, CourseAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('userId', 'post', 'comment', 'date')

admin.site.register(Comment, CommentAdmin)

