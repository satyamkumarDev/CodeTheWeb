from django.shortcuts import render, HttpResponse

# Create your views here.

def blogHome(request):
   return render(request, 'Blog/blogHome.html')
   # return HttpResponse('BlogHome')

def blogPost(request, slug):
   return render(request, 'Blog/blogPost.html')
   # return HttpResponse(f'Blog Post:{slug}')