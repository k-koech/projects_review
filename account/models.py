from django.db import models
import datetime as dt
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from cloudinary.models import CloudinaryField
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError(" User must have an email address")
        if not username:
            raise ValueError(" User must have an username!")    
        
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password = password,
            username=username,
        )
        user.email = email
        user.is_admin = True 
        user.is_staff = True 
        user.is_superuser = True 
        user.save(using=self._db)
        return user
        

class Users(AbstractBaseUser):
    username = models.CharField( max_length=80, unique=True)  
    email = models.CharField( max_length=100, unique=True) 
    phone_number = models.CharField(max_length = 15,blank =True)
    profile_photo = CloudinaryField('image', default='image/upload/v1631717620/default_uomrne.jpg') 
    bio= models.TextField(null=True)
    linkedin= models.CharField(max_length=50, null=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(default=dt.datetime.now)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    password_reset = models.CharField( max_length=50, default="e5viu3snjorndvd")    
    password = models.CharField( max_length=100)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [ 'username']
    
    objects=MyAccountManager()
     
    def _str_(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
    def save_project(self):
        self.save()
    
    @classmethod
    def delete_user(cls,id):
        delete_user = cls.objects.get(id=id)
        delete_user.delete()
        return delete_user
    
    @classmethod
    def update_user(cls,id,profile_photo,bio, phone_number):
        user=cls.objects.get(id=id)
        user.profile_photo=profile_photo
        user.bio=bio
        user.profile_photo=profile_photo
        user.bio=bio
        user.phone_number=phone_number
        return user.save()


class Projects(models.Model):
    title = models.CharField(max_length =200)
    image = CloudinaryField('image', default='image/upload/v1631717620/default_uomrne.jpg') 
    description = models.TextField()
    link = models.CharField(max_length =200)
    languages = ArrayField(models.CharField(max_length=50,null=True, default=[]),size=20 )
    date_posted = models.DateTimeField(verbose_name='date posted', auto_now_add=True)
    user=models.ForeignKey("Users",on_delete=models.CASCADE)

    def save_project(self):
        self.save()
    
    @classmethod
    def update_project(cls,id,description,title,image):
        get_project=cls.objects.get(id=id)
        get_project.title=title
        get_project.description=description
        get_project.image=image
        return get_project.save()
    
    @classmethod
    def delete_project(cls,id):
        delete_project = cls.objects.get(id=id)
        delete_project.delete()
        return delete_project

class Review(models.Model):
    date_voted = models.DateTimeField(verbose_name='date posted', auto_now_add=True)
    design=models.FloatField(default=0)
    usability=models.FloatField(default=0)
    content=models.FloatField(default=0)
    project=models.ForeignKey("Projects",on_delete=models.CASCADE)
    user=models.ForeignKey("Users",on_delete=models.CASCADE)

    def save_review(self):
        self.save()
    
    @classmethod
    def update_review(cls,id,design,content,usability):
        get_review=cls.objects.get(id=id)
        get_review.design=design
        get_review.usability=usability
        get_review.content=content
        return get_review.save()
    
    @classmethod
    def delete_review(cls,id):
        delete_review = cls.objects.get(id=id)
        delete_review.delete()
        return delete_review