from django.contrib import admin
from .models import Class, Review, Genre

# Register your models here.

class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(Genre, GenreAdmin)

class ClassAdmin(admin.ModelAdmin):
    list_display = ('userId', 'title', 'body', 'userId_id', 'genreName')

admin.site.register(Class, ClassAdmin)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('userId', 'clazz', 'review', 'date')

admin.site.register(Review, ReviewAdmin)