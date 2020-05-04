from django.shortcuts import render, HttpResponse
from home.models import Contact
from django.contrib import messages
from Blog.models import Post
# Create your views here.

def home(request):
    posts=Post.objects.all()
    homepost={'posts':posts}
    return render(request, 'home/home.html', homepost)

def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        email = request.POST['email']
        mob = request.POST['mobile']
        content= request.POST['content']

        if len(name)<3 or len(email)<5 or len(mob)<10 or len(content)<10:
            messages.error(request,"Please fill the form Correctly!")
        else:
            contact=Contact(name=name, email=email, mobile=mob, content=content)
            contact.save()
            messages.success(request, "welcome to MyBlog!")

    return render(request, 'home/contact.html')

def about(request):
    return render(request, 'home/about.html')