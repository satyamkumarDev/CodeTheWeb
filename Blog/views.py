from django.shortcuts import render, HttpResponse, redirect
from Blog.models import Post, BlogComment
from django.contrib import messages

# Create your views here.

def blogHome(request):
   allposts=Post.objects.all()
   context={'allposts':allposts}
   return render(request, 'Blog/blogHome.html', context)


def blogPost(request, slug):
   post=Post.objects.filter(slug=slug).first()
   comments=BlogComment.objects.filter(post=post)
   context={'post':post, 'comments':comments}
   return render(request, 'Blog/blogPost.html', context)

def postComment(request):
   if request.method=='POST':
      comment=request.POST.get("comment")
      user=request.user
      postId=request.POST.get("postSno")
      post=Post.objects.get(post_id=postId)

      comment=BlogComment(comment=comment, user=user, post=post)
      comment.save()
      messages.success(request, 'Your comment has been added successfully')

   return redirect(f"/blog/{Post.slug}")

