from django.contrib import admin
from .models import BlogArticles

class BlogArticlesAdmin(admin.ModelAdmin):
    list_display=("title","author","publish") #�б�ͷ
    list_filter=("publish","author") #ɸѡ
    search_fields=("title","body") #������Χ
    raw_id_fields=("author",)
    date_hierarchy="publish"  #���ڷּ�
    ordering=['publish','author'] #�������
    
# Register your models here.
admin.site.register(BlogArticles,BlogArticlesAdmin)