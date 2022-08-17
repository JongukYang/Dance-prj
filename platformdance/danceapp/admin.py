from django.contrib import admin
from .models import Post, Comment, Genre, Course

# Register your models here.

# 장르 모델
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
admin.site.register(Genre, GenreAdmin)

# 영상 게시글
class PostAdmin(admin.ModelAdmin):
    list_display = ('id','userId', 'userId_id', 'title', 'body', 'genreName', 'hits', 'likes_count', 'uploadDate', 'updateDate')
admin.site.register(Post, PostAdmin)

# 클래스 게시글
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'userId', 'userId_id', 'title', 'body', 'genreName','hits', 'likes_count', 'startDate', 'register_count','maxRegCount', 'location', 'uploadDate', 'updateDate')
admin.site.register(Course, CourseAdmin)

# 댓글
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'userId', 'post', 'comment', 'date')
admin.site.register(Comment, CommentAdmin)

