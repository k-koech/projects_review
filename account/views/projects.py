from django.contrib.messages.api import add_message
from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from ..models import Projects, Users
from django.contrib.auth import authenticate,login,logout,login
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from rest_framework.response import Response
from rest_framework.views import APIView
from ..serializer import MerchSerializer, MerchUser

# Create your views here.
class MerchList(APIView):
    def get(self, request, format=None):
        projects = Projects.objects.all()
        serializers = MerchSerializer(projects, many=True)
        return Response(serializers.data)

class MerchUsers(APIView):  
    def get(self, request, format=None):
        users = Users.objects.all()
        serializers = MerchUser(users, many=True)
        return Response(serializers.data)
# ..........................................................


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
        user = Users.objects.get(id=request.user.id)

        email=request.POST['email']
        username=request.POST['username']
        bio=request.POST['bio']
        phone_number=request.POST['phone_number']
      
        user.email=email
        user.bio=bio
        user.username=username
        user.phone_number=phone_number
        user.save()

        messages.add_message(request, messages.SUCCESS, "Profile saved successfully")
        return redirect(profile)

     else:
        return render(request, "profile.html")

""" UPDATE PROFILE PHOTO VIEW """  
def profile_photo(request):   
    if request.method=="POST":
        user=Users.objects.get(id=request.user.id)
        profile_img=request.FILES.get('file') 

        print(profile_img)
        user.profile_photo=profile_img
        user.save()      
        return JsonResponse({"msg":"Saved successfully", "success":"success"})
              
    else:
        pass