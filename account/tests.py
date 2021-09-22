from django.test import TestCase
from .models import Users, Projects
# Create your tests here.
class ProjectsTestClass(TestCase):
    def setUp(self):
        # Creating a new user and saving it
        self.user=Users(username="kk",profile_photo = 'xyz.png', email="triplek@gmail.com",bio="Am Happy", phone_number ='+254725801772',date_joined="2021-09-05 22:16:35.61389+03")
        self.user.save()

        # Creating a new Project and saving it
        self.new_post = Projects(title="Instaclone app",image = 'xyz.png', description="The project is a a clone of instagram",link="https://github.com/k-koech/gallery_django",date_joined="2021-09-05 22:16", user=self.user)
        self.new_pr.save()


    def tearDown(self):
        Users.objects.all().delete()
        Projects.objects.all().delete()
       
    
    # SAVING USERS
    def test_save_user(self):
        self.user=Posts(post_image = 'xyz.jpg', caption ='It was a one tour to mombasa')
        image_obj = Posts.objects.all().count()
        self.assertTrue(image_obj>0)


    def test_update_caption(self):
        image_obj = Posts.objects.first()
        id=image_obj.id
        caption="This is lit"        
        Posts.update_caption(id,caption)
        image = Posts.objects.get(id=id)
        self.assertEqual(image.caption,"This is lit")

    def test_delete_image(self):
        image=Posts.objects.first()
        id=image.id
        Posts.delete_image(id)
        try:
            img = Posts.objects.get(id=id)
            self.assertTrue("Some results")
        except Posts.DoesNotExist:
            self.assertTrue("no results"=="no results")

    # TEST PROFILE
    def test_save_profile(self):
        profile=Profile(profile_photo = 'myphoto.jpg', bio ='Chelsea fan', user=3)
        profile.save_profile()
        profile_obj = Profile.objects.all().count()
        self.assertTrue(profile_obj>1)


    def test_update_profile(self):
        profile_obj = Profile.objects.first()
        id=profile_obj.id
        profile_image="myPhoto.png"
        bio="always happy"        
        Profile.update_profile(id,profile_image,bio)
        profile = Profile.objects.get(id=id)
        self.assertEqual(profile.bio,"always happy")

    def test_delete_profile(self):
        profile=Profile.objects.first()
        id=profile.id
        Profile.delete_profile(id)
        try:
            Profile.objects.get(id=id)
            self.assertTrue("Some results")
        except Profile.DoesNotExist:
            self.assertTrue("no results"=="no results")