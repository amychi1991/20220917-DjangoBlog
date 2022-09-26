from gc import get_objects
from operator import index
from urllib.request import Request
from django.shortcuts import render, get_object_or_404
#from django.http import HttpResponse
from datetime import datetime
from .models import BlogArticles

# Create your views here.
def index(request):
    now = datetime.now()
   # html_content="hello django"
    #html_content = "<html><head><title>Hello, Django</title></head><body>"
    #html_content += "<strong>Hello Django!</strong> on " + now.strftime("%A, %d %B, %Y at %X")
    #html_content += "</body></html>"

    #return HttpResponse(html_content)
    return render(
        request,
        "blog/index.html",
        {
           # 'content': "<strong>Hello Django!</strong> on " + now.strftime("%A, %d %B, %Y at %X")
           'title':"hello Django",
           'message':"hello django!",
           'content':" on " + now.strftime("%A, %d %B, %Y at %X")
        }
    )

def blog_title(request):
    blogs=BlogArticles.objects.all()
    return render(request,"blog/titles.html",{"blogs":blogs})

def blog_article(request,article_id):
    #article=BlogArticles.objects.get(id=article_id)
    article =get_object_or_404(BlogArticles,id=article_id)
    pub=article.publish
    return render(request,"blog/content.html",{"article":article,"publish":pub})
   