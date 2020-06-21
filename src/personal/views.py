from django.shortcuts import render
from blog.models import BlogPost
from operator import attrgetter

from blog.views import get_blog_queryset

# Create your views here.

def home_screen_view(request): 
    context={}
    
    query =""
    if request.GET:
        query = request.GET['q']
        context['query'] = str(query)

    blog_post = sorted(get_blog_queryset(query), key= attrgetter('date_updated'), reverse= True)
    context['blog_posts'] = blog_post
    return render(request,"personal/home.html", context)