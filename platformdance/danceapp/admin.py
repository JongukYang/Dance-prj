from django.contrib import admin
from .models import Post, Comment

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('userId', 'title', 'body', 'uploadDate', 'updateDate')

admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment', 'date', 'post', 'userId')

admin.site.register(Comment, CommentAdmin)