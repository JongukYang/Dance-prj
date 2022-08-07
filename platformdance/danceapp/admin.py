from django.contrib import admin
from .models import Post, Comment, Genre, Course

# Register your models here.

class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(Genre, GenreAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ('userId', 'title', 'body', 'userId_id', 'genreName', 'uploadDate', 'updateDate')

admin.site.register(Post, PostAdmin)

class CourseAdmin(admin.ModelAdmin):
    list_display = ('userId', 'title', 'body', 'userId_id', 'genreName', 'uploadDate', 'updateDate', 'startDate')

admin.site.register(Course, CourseAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('userId', 'post', 'comment', 'date')

admin.site.register(Comment, CommentAdmin)

