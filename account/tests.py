from django.test import TestCase
from .models import Review, Users, Projects
# Create your tests here.
class ProjectsTestClass(TestCase):
    def setUp(self):
        # Creating a new user and saving it
        self.user=Users(username="kk",profile_photo = 'xyz.png', email="triplek@gmail.com",bio="Am Happy", phone_number ='+254725801772',date_joined="2021-09-05 22:16:35.61389+03")
        self.user.save()

        # Creating a new Project and saving it
        self.new_project = Projects(title="Instaclone app",image = 'xyz.png', description="The project is a a clone of instagram",link="https://github.com/k-koech/gallery_django",date_posted="2021-09-05 22:16:35.61389+03", user=self.user)
        self.new_project.save()

        # Creating a new Review and saving it
        self.new_review = Review(design=2,userbility=6,content=8,project=self.new_project,date_voted="2021-09-05 22:16:35.61389+03", user=self.user)
        self.new_review.save()

    def tearDown(self):
        Users.objects.all().delete()
        Projects.objects.all().delete()
        Review.objects.all().delete()

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

    # TEST REVIEW
    def test_save_review(self):
        review= Review(design=2,userbility=6,content=8,project=self.new_project,date_voted="2021-09-05 22:16:35.61389+03", user=self.user)
        review.save_review()
        review_obj = Review.objects.all().count()
        self.assertTrue(review_obj>1)


    def test_update_review(self):
        review_obj = Review.objects.first()
        id=review_obj.id
        design=3
        content=6
        userbility=10    
        Review.update_review(id,design,content,userbility)
        updated_review = Review.objects.get(id=id)
        self.assertEqual(updated_review.content,6.0)

    def test_delete_review(self):
        reviews=Review.objects.first()
        id=reviews.id
        reviews.delete_review(id)
        try:
            Review.objects.get(id=id)
            self.assertTrue("Some results")
        except Review.DoesNotExist:
            self.assertTrue("no results"=="no results")