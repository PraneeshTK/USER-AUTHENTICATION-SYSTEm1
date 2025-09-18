from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate ,login,logout
# Create your views here.
def home(request):
    return render(request,"index.html")

def signup(request):
    if request.method == "POST":
        #username = request.POST.get('username')
        username =request.POST.get('username')
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('lname')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2') 
        
        if User.objects.filter(username =username):
            messages.error(request,"User already exist! Please try some other username")
            return redirect('home')
        if User.objects.filter(email=email):
            messages.error(request,"Email already registered")
            return redirect('home')
        if len(username)>20:
            messages.error(request,"Username must be under 20 characters")
        
        if pass1 != pass2:
            messages.error(request,"Passwords didn't match")
            return redirect('signup')
        
        if not username.isalnum():
            messages.error(request,"User name must be alpha-Numeric")
            return redirect('home')
        
        
        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        
        myuser.save()
        
        messages.success(request,"Your Account has been successfully created.")
        return redirect('signin')
    
    
    return render(request,"signup.html")

def signin(request):
    if request.method=="POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        user = authenticate(username = username,password =pass1)
        
        if user is not None:
            login(request,user)
            fname = user.first_name
            return render(request,"index.html",{"fname":fname})
        else:
            messages.error(request,"You have entered wrong username or password")
            return redirect('signin')
    return render(request,"signin.html")

def signout(request):
    logout(request)
    messages.success(request,"Logged Out Successfully")
    return redirect('home')