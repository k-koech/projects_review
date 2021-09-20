from django.contrib.messages.api import add_message
from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from ..models import Projects, Users
from django.contrib.auth import authenticate,login,logout,login
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
""" ADD PROJECT VIEW """  
def add_project(request):   
    if request.method=="POST":
        title=request.POST['title']
        link=request.POST['link']
        description=request.POST['description']
        image=request.FILES['image']

        user = Projects(title=title, description=description,link=link,image=image,user=request.user)
        user.save()
        messages.add_message(request, messages.SUCCESS, "Saved successfully!!")
        return redirect(add_project)

            
    else:
        return render(request, "add_project.html")
         

""" PROFILE VIEW """
def profile(request):
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
        return render(request, "profile.html")


