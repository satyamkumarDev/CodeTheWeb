from django.shortcuts import render, HttpResponse

# Create your views here.

def blogHome(request):
   return HttpResponse('BlogHome')

def blogPost(request, slug):
   return HttpResponse(f'Blog Post:{slug}')