from django.contrib import admin
from .models import Post, Comment, Genre

# Register your models here.

class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(Genre, GenreAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ('userId', 'title', 'body', 'uploadDate', 'updateDate', 'userId_id', 'genreName')

admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment', 'date', 'post', 'userId')

admin.site.register(Comment, CommentAdmin)

