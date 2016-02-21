from django.contrib import admin
from .models import Movie, Comment

# Register your models here.

class CommentInline(admin.StackedInline):
    model = Comment

class MovieAdmin(admin.ModelAdmin):
    inlines = [CommentInline,]

admin.site.register(Movie, MovieAdmin)
admin.site.register(Comment)