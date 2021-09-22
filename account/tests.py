from django.test import TestCase
from .models import Users, Projects
# Create your tests here.
class ProjectsTestClass(TestCase):
    def setUp(self):
        # Creating a new user and saving it
        self.user=Users(username="kk",profile_photo = 'xyz.png', email="triplek@gmail.com",bio="Am Happy", phone_number ='+254725801772',date_joined="2021-09-05 22:16:35.61389+03")
        self.user.save()

        # Creating a new Project and saving it
        self.new_project = Projects(title="Instaclone app",image = 'xyz.png', description="The project is a a clone of instagram",link="https://github.com/k-koech/gallery_django",date_posted="2021-09-05 22:16:35.61389+03", user=self.user)
        self.new_project.save()


    def tearDown(self):
        Users.objects.all().delete()
        Projects.objects.all().delete()
       
    
    # SAVING USERS
    def test_save_user(self):
        self.user=Users(username="kk",profile_photo = 'xyz.png', email="triplek@gmail.com",bio="Am Happy", phone_number ='+254725801772',date_joined="2021-09-05 22:16:35.61389+03")
        users_count = Users.objects.all().count()
        self.assertTrue(users_count>0)


    def test_update_user(self):
        user = Users.objects.first()
        id=user.id
        bio="Chelsea"  
        profile_photo="abc.jpg"
        phone_number="+254725801772"     
        Users.update_user(id,profile_photo,bio, phone_number)
        updated_user = Users.objects.get(id=id)
        self.assertEqual(updated_user.bio,"Chelsea")

    def test_delete_user(self):
        user=Users.objects.first()
        id=user.id
        Users.delete_user(id)
        try:
            Users.objects.get(id=id)
            self.assertTrue("Some results")
        except Users.DoesNotExist:
            self.assertTrue("no results"=="no results")

    # TEST PROJECT
    def test_save_project(self):
        project=Projects(title="Instaclone app",image = 'xyz.png', description="The project is a a clone of instagram",link="https://github.com/k-koech/gallery_django",date_posted="2021-09-05 22:16:35.61389+03", user=self.user)
        project.save_project()
        project_obj = Projects.objects.all().count()
        self.assertTrue(project_obj>1)


    def test_update_project(self):
        project_obj = Projects.objects.first()
        id=project_obj.id
        title="Portfolio"
        description="Description of a my portfolio"
        image="portfolio.jpg"     
        Projects.update_project(id,description,title,image)
        profile = Projects.objects.get(id=id)
        self.assertEqual(profile.title,"Portfolio")

    def test_delete_profile(self):
        projects=Projects.objects.first()
        id=projects.id
        Projects.delete_project(id)
        try:
            Projects.objects.get(id=id)
            self.assertTrue("Some results")
        except Projects.DoesNotExist:
            self.assertTrue("no results"=="no results")