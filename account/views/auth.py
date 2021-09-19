from django.shortcuts import render, redirect
from ..models import Users
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.hashers import make_password


# Create your views here.
def index(request):
    return render(request,'index.html')

""" USER REGISTRATION VIEW """  
def register(request):   
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']

        username_exist=Users.objects.filter(username=username).count()
        email_exist=Users.objects.filter(email=email).count()
        if username_exist<1:
            if email_exist<1:
                if password==confirm_password:
                    user = Users(username=username, email=email,followers=[],following=[], password=make_password(password))
                    user.save()

                    user = Users.objects.get(username=username)
                   

                    messages.add_message(request, messages.SUCCESS, 'Successfully Registered!')
                    return redirect(signIn)
                else:
                    messages.add_message(request, messages.ERROR, "Password doesn't match ")
                    return redirect(register)
            else:
                    messages.add_message(request, messages.ERROR, "Email exist!")
                    return redirect(register)
        else:
                messages.add_message(request, messages.ERROR, "Username exist!! ")
                return redirect(register)
    else:
        return render(request, "register.html")

""" LOGIN VIEW """
def signIn(request):
     if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        user= authenticate(email=email, password=password)

        if user is not None:
            login(request,user )
            messages.add_message(request, messages.INFO, 'Successfully logged in!')
            return redirect(index)
 
        else:
            messages.add_message(request, messages.ERROR, 'Invalid Credentials')
            return redirect(signIn)

     else:
        return render(request, "index.html")

""" LOGOUT VIEW """
def signOut(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, 'Logout successfully!')
    return redirect(signIn)
