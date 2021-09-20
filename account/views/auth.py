from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from ..models import Projects, Users
from django.contrib.auth import authenticate,login,logout,login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.hashers import make_password


# Create your views here.
def index(request):
    projects=Projects.objects.all()
    context={"projects":projects}
    return render(request,'index.html', context)

""" USER REGISTRATION VIEW """  
def register(request):   
    if request.method=="POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')

        username_exist=Users.objects.filter(username=username).count()
        email_exist=Users.objects.filter(email=email).count()
        if username_exist<1:
            if email_exist<1:
                if password==confirm_password:
                    user = Users(username=username, email=email,phone_number=phone, password=make_password(password))
                    user.save()

                    user = Users.objects.get(username=username)
                    return JsonResponse({"msg":"Registered successfully", "success":"success"})
                   
                else:
                    return JsonResponse({"msg":"Password doesn't match", "error":"password_match" })
                
            else:
                    return JsonResponse({"msg":"Email exist", "error":"email"})
                
        else:
                return JsonResponse({"msg":"Username exist.", "error":"username"})
              
    else:
        pass

""" LOGIN VIEW """
def signIn(request):
     if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        user= authenticate(email=email, password=password)

        if user is not None:
            login(request,user )
            return JsonResponse({"msg":"Login succcess", "success":"success"})
            # messages.add_message(request, messages.INFO, 'Successfully logged in!')
            # return redirect(index)
 
        else:
            return JsonResponse({"msg":"Invalid Credentials", "error":"credentials"})

     else:
        pass

""" LOGOUT VIEW """
def signOut(request):
    logout(request)
    # messages.add_message(request, messages.SUCCESS, 'Logout successfully!')
    return redirect(index)
