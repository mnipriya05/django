from django.contrib import admin
from .models import Post, Category, Comment, Like

admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Like)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at')
    fields = ('title', 'content', 'category')