from django.shortcuts import render, HttpResponse
from Blog.models import Post
# Create your views here.

def blogHome(request):
   allposts=Post.objects.all()
   context={'allposts':allposts}
   return render(request, 'Blog/blogHome.html', context)


def blogPost(request, slug):
   post=Post.objects.filter(slug=slug).first()
   context={'post':post}
   return render(request, 'Blog/blogPost.html', context)
