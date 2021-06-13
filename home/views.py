from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login
from home.models import Contact
from django.contrib import messages
from blog.models import Post
import requests
import json
from django.http import JsonResponse
from nsetools import Nse
# Create your views here.
def home(request):
    nse = Nse()
    index_codes = nse.get_index_list()
    #print(index_codes)
    return render(request,'index.html',
         {'index_codes':index_codes}
    )

def about(request):
    return render(request, 'home/about.html')
    
def services(request):
    return render(request, 'services.html')
    #return HttpResponse("this is services page")
def contact(request):
    #messages.error(request, 'Welcome to Contact')
    if request.method == "POST" :
        name = request.POST['name']
        email= request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        #print(name,email,phone,content)
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4 :
            messages.error(request,"Please fill the form correctly")
        else:
            contact = Contact(name= name, email= email, phone= phone , content = content )
            contact.save()
            messages.success(request,"Your message has been sent succesfully")

    return render(request, 'home/contact.html')
def handleSignup(request):
    if request.method == 'POST' :
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        #checks
        if len(username) > 10 :
            messages.error(request, "Username must be under 10 characters")
            return redirect('home')
        if not username.isalnum() :
            messages.error(request, "Username should only contain letters and numbers")
            return redirect('home')
        if pass1 !=pass2:
             messages.error(request, "Passwords must be same")
             return redirect('home')
        

        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname    
        myuser.last_name = lname    
        myuser.save()
        messages.success(request,"Your Bull Traders account is created successfully !")
        return redirect("home")
    else:
        return HttpResponse('404_ Not Found')
   
def handleLogin(request):
    if request.method == "POST" :
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        #check if user has entered correct credentials
        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
    # A backend authenticated the credentials
             login(request,user)
             messages.success(request," Successfully Logged In !")
             return redirect("home")
        else:
            # No backend authenticated the credentials
             messages.error(request,"Invalid credentials , please try again !")
             return render(request, 'home')
    return HttpResponse('handleLogin')
    #return render(request, 'login.html')
def handleLogout(request):
    logout(request)
    messages.success(request," Successfully Logged OUT !")
    return redirect("home")
    return HttpResponse(request, 'handelLogout')
def search(request):
    query = request.GET['query']
    if len(query)>78:
        allPosts = Post.objects.none()
    else :
        allPostsTitle = Post.objects.filter(title__icontains=query)
        allPostsContent = Post.objects.filter(content__icontains=query)
        allPosts = allPostsTitle.union(allPostsContent)
    if allPosts.count() == 0:
        messages.warning(request,"No search result found Please refine your query")
    params = {'allPosts': allPosts,'query':query}
    return render(request, 'home/search.html',params)
