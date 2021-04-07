from django.test import TestCase
from .models import *
import datetime as dt
from django.contrib.auth.models import User

class UserTestClass(TestCase):

# Set up method
    def setUp(self):
        self.rose= User(username = 'Rose', password = '123456789')

# Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.rose,User))

class ProjectTestClass(TestCase):
    
    def setUp(self):
        # Creating a new user and saving it
        self.rose= user(first_name = 'Rose', last_name ='Okoth', email ='okoth.rose@gmail.com')
        self.rose.save_user()

        # Creating a new tag and saving it
        self.new_slug = slug(name = 'testing')
        self.new_slug.save()
        self.new_post= Post(title = 'Test Post',content = 'This is a random test',editor = self.rose)
        self.new_post.save()
        self.new_post.slug.add(self.new_slug)

        def tearDown(self):
            User.objects.all().delete()
            Post.objects.all().delete()

class TestProfile(TestCase):
    def setUp(self):
        self.user = User(username='mimi', password='passw0rd')
        self.user.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))

    def test_save_user(self):
        self.user.save()

    def test_delete_user(self):
        self.user.delete()


# class ProjectTest(TestCase):
#     def setUp(self):
#         self.user = User.objects.create(username='mimi')
#         self.project = Project.objects.create(title='project', image='https://picture.com', description='description', link='http://url.com')

#     def test_instance(self):
#         self.assertTrue(isinstance(self.project, Project))

#     def test_save_project(self):
#         self.project.save_project()
#         project = Project.objects.all()
#         self.assertTrue(len(project) > 0)

#     def test_get_projects(self):
#         self.project.save()
#         projects = Project.all_projects()
#         self.assertTrue(len(projects) > 0)

#     def test_search_project(self):
#         self.project.save()
#         project = Project.search_project('test')
#         self.assertTrue(len(project) > 0)

#     def test_delete_project(self):
#         self.project.delete_project()
#         project = Project.search_project('test')
#         self.assertTrue(len(project) < 1)


# class RatingTest(TestCase):
#     def setUp(self):
#         self.user = User.objects.create(username='mimi')
#         self.project = Project.objects.create(title='project', image='https://picture.com', slug='slug', description='description', link='http://url.com')
#         self.rating = Rating.objects.create(design=6, usability=7, content=9, user=self.user, project=self.project)

#     def test_instance(self):
#         self.assertTrue(isinstance(self.rating, Rating))

#     def test_save_rating(self):
#         self.rating.save_rating()
#         rating = Rating.objects.all()
#         self.assertTrue(len(rating) > 0)

#     def test_get_project_rating(self, slug=None):
#         self.rating.save()
#         rating = Rating.get_ratings(project_slug=slug)
#         self.assertTrue(len(rating) == 1)