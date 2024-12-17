from django.shortcuts import render
from .models import Post

def blog_list(request):
    post = Post.objects.all()
    context = {
        'blog_list':post  #this var name needs to match the one in this func
        }
    return render(request,"blog/blog_list.html", context)