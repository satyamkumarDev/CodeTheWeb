from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact
from django.contrib import messages
from Blog.models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
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

def search(request):
    querry=request.GET['querry']
    if len(querry)>30:
        allposts=Post.objects.none()
    else:
        allpostTitle=Post.objects.filter(title__icontains=querry)
        allpostContent=Post.objects.filter(content__icontains=querry)
        allposts=allpostTitle.union(allpostContent)
    if allposts.count() == 0:
        messages.warning(request,'No search results Found, Please refine your query')
    posts={'allposts':allposts, 'querry':querry}
    return render(request,'home/search.html',posts)

def handleSignup(request):
    if request.method=='POST':
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        password=request.POST['pass']
        cpassword=request.POST['cpass']

        # Check the inputs

        if len(username)>15:
            messages.error(request, "Username must be small")
            return redirect('home')
        if not username.isalnum():
            messages.error(request, 'Username must include letter and numbers of theese chars A-Z, a-z, 0-9')
            return redirect('home')
        if password != cpassword:
            messages.error(request, "password do not match")
            return redirect('home')

        newUser=User.objects.create_user(username, email, password)
        newUser.first_name=fname
        newUser.last_name=lname
        newUser.save()
        messages.success(request, 'Your Account has been created successfully!')
        return redirect('home')
    else:
        return HttpResponse('404 - Not Found')

def handleLogin(request):
    if request.method=='POST':
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpass']
        user= authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request,user)
            messages.success(request, 'Successfully logged In')
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials, Please try again!')
            return redirect('home')
    else:
        return HttpResponse('404- Not Found')

def handleLogout(request):
    logout(request)
    messages.success(request, 'Successfully logged out!')
    return redirect('home')