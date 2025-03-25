# from django.test import TestCase

# Create your tests here.
from django.test import TestCase 
from .models import Post 
from django.urls import reverse

class PostTests(TestCase):
    @classmethod 
    def setUpTestData(cls):
        cls.p=Post.objects.create(text="This is a test!")
    
    def test_model_item(self):
        self.assertEqual(self.p.text,"This is a test!")
    
    def test_url_of_exist(self):
        response=self.client.get("/")
        self.assertEqual(response.status_code,200)

    # def test_url_name(self):
    #     response=self.client.get(reverse("post_l"))
    #     self.assertEqual(response.status_code,200)
    
    # def test_template_name(self):
    #     response=self.client.get(reverse("post_l"))
    #     self.assertTemplateUsed(response,"posts_list.html")
    
    # def test_template_content(self):
    #     response=self.client.get(reverse("post_l"))
    #     # print(response)
    #     self.assertContains(response,"This is a test!")

    def test_url_name_template_content(self):
        response=self.client.get(reverse("post_l"))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,"posts_list.html")
        self.assertContains(response,"This is a test!")