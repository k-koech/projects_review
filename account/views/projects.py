from account.views.auth import index
from django.contrib.messages.api import add_message
from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..models import Projects, Review, Users
from django.contrib.auth import login as django_login,logout as django_logout,login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Avg

from rest_framework.response import Response
from rest_framework.views import APIView
from ..serializer import LoginSerializer, MerchSerializer, MerchUser
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import GenericAPIView
from rest_framework.authtoken.models import Token


# Create your views here.
class MerchList(APIView):
    def get(self, request, format=None):
        projects = Projects.objects.all()
        serializers = MerchSerializer(projects, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = MerchSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class MerchUsers(APIView):  
    def get(self, request, format=None):
        users = Users.objects.all()
        serializers = MerchUser(users, many=True)
        return Response(serializers.data)
    
class LoginView(GenericAPIView):
    serializer_class = LoginSerializer
    
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        django_login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key}, status=200)


class LogoutView(APIView):
    authentication_classes = (TokenAuthentication, )

    def post(self, request):
        django_logout(request)
        return Response(status=204)
# ..........................................................

@login_required(login_url='/')
def add_project(request):   
    """ ADD PROJECT VIEW """  
    if request.method=="POST":
        title=request.POST['title']
        link=request.POST['link']
        description=request.POST['description']
        image=request.FILES['image']
        languages=request.POST.getlist("language[]")
        for i in languages:
            print(i)
        user = Projects(title=title, description=description,link=link,languages=languages,image=image,user=request.user)
        user.save()
        messages.add_message(request, messages.SUCCESS, "Saved successfully!!")
        return redirect(add_project)
            
    else:
        return render(request, "add_project.html")

@login_required(login_url='/')   
def rate_project(request,id):
    """RATE PROJECT VIEW"""
    if request.method=="POST":
        project = Projects.objects.get(id=id)

        rev = Review.objects.filter(project__id=id, user__id=request.user.id).count()
        if rev>0:
            return JsonResponse({"msg":"You have already rated!", "error":"error"})

        design=request.POST.get('design')
        usability=request.POST.get('usability')
        content=request.POST.get('content')
        review=Review(design=design, usability=usability, content=content, project=project, user=request.user)
        review.save()
    return JsonResponse({"msg":"Rated successfuly.", "success":"success"})

@login_required(login_url='/')   
def delete_project(request,id):
    project=Projects.objects.get(id=id)
    project.delete()
    return redirect(index)

@login_required(login_url='/')     
def project(request, id):
    project = Projects.objects.get(id=id)
    no_of_review = Review.objects.filter(project__id=id).count()

    avg_design= Review.objects.filter(project__id=project.id).aggregate(Avg('design'))
    avg_usability= Review.objects.filter(project__id=project.id).aggregate(Avg('usability'))
    avg_content= Review.objects.filter(project__id=project.id).aggregate(Avg('content'))

    if avg_content["content__avg"]==None or avg_design["design__avg"]==None or avg_usability["usability__avg"]==None:
        print("No value")
        return render(request, 'project.html', {'reviews':0,"project":project} )

    else:
        avg_content=round((avg_content["content__avg"]), 2)
        avg_design=round(avg_design["design__avg"], 2)
        avg_usability=round(avg_usability["usability__avg"], 2)
        
        average= round((avg_content+avg_usability+avg_design)/3, 2)

        context = {"project":project,"usability":avg_usability,"design":avg_design, "content":avg_content, "average":average,"no_of_review":no_of_review}
        return render(request, 'project.html', context )

login_required(login_url='/')     
def search(request):
    """SEARCH VIEW"""
    title=request.POST.get('search')
    # project = Projects.objects.get(title__contains=title)

    try:
        project = Projects.objects.get(title__contains=title)
    except Projects.DoesNotExist:
        return redirect(fouroffour_not_found)

    project = Projects.objects.get(title__contains=title)

    avg_design= Review.objects.filter(project__id=project.id).aggregate(Avg('design'))
    avg_usability= Review.objects.filter(project__id=project.id).aggregate(Avg('usability'))
    avg_content= Review.objects.filter(project__id=project.id).aggregate(Avg('content'))

    if avg_content["content__avg"]==None or avg_design["design__avg"]==None or avg_usability["usability__avg"]==None:
        print("No value")
        return render(request, 'search.html', {'reviews':0,"project":project} )

    else:
        avg_content=round((avg_content["content__avg"]), 1)
        avg_design=round(avg_design["design__avg"], 1)
        avg_usability=round(avg_usability["usability__avg"], 1)
        
        average= round(int(avg_content+avg_usability+avg_design)/3, 1)

        context = {"project":project,"usability":avg_usability,"design":avg_design, "content":avg_content, "average":average}
        return render(request, 'search.html', context )


@login_required(login_url='/')
def profile(request):
     """ PROFILE VIEW """
     if request.method=="POST":
        user = Users.objects.get(id=request.user.id)

        email=request.POST['email']
        username=request.POST['username']
        bio=request.POST['bio']
        linkedin=request.POST['linkedin']
        phone_number=request.POST['phone_number']
      
        user.email=email
        user.bio=bio
        user.username=username
        user.linkedin=linkedin
        user.phone_number=phone_number
        user.save()

        messages.add_message(request, messages.SUCCESS, "Profile saved successfully")
        return redirect(profile)
     else:
        projects=Projects.objects.filter(user__id=request.user.id).order_by("-date_posted")
        counter=Projects.objects.filter(user__id=request.user.id).count()

        context={"projects":projects,"counter":counter}
        print(projects)
        print(request.user.id)
        return render(request, "profile.html", context)


@login_required(login_url='/')
def profile_photo(request):
    """ UPDATE PROFILE PHOTO VIEW """     
    if request.method=="POST":
        user=Users.objects.get(id=request.user.id)
        profile_img=request.FILES['profile_photo']

        print(profile_img)
        user.profile_photo=profile_img
        user.save()      
    return redirect(profile)
  

def  fouroffour_not_found(request):
    return render(request, "four_of_four.html")
