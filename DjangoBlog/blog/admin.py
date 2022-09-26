from django.contrib import admin
from .models import BlogArticles

class BlogArticlesAdmin(admin.ModelAdmin):
    list_display=("title","author","publish") #列表头
    list_filter=("publish","author") #筛选
    search_fields=("title","body") #搜索范围
    raw_id_fields=("author",)
    date_hierarchy="publish"  #日期分级
    ordering=['publish','author'] #排序规则
    
# Register your models here.
admin.site.register(BlogArticles,BlogArticlesAdmin)