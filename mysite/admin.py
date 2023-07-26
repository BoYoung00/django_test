from django.contrib import admin
from .models import MainContent, Comment

class MainContentAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'pub_date']
    search_fields = ['title']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['content_list', 'content', 'author', 'create_date', 'modify_date']
    search_fields = ['author']

# 관리자 페이지에서 MainContent를 조작
admin.site.register(MainContent, MainContentAdmin)
admin.site.register(Comment, CommentAdmin)
