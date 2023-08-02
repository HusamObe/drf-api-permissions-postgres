from django.test import TestCase

# Create your tests here.
from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from .models import Comic
# Create your tests here.
class ComicTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )
        testuser1.save()
        testuser2 = get_user_model().objects.create_user(
            username="testuser2", password="pass2"
        )
        testuser2.save() 

    

        test_comic = Comic.objects.create(
            title="rake",
            owner=testuser1,
            desc="Better for collecting leaves than a shovel.",
        )
        test_comic.save()

    def setUp(self) -> None:
         self.client.login(username="testuser1", password="pass")  

   
    def test_comics_model(self):
        comic = Comic.objects.get(id=1)
        actual_owner = str(comic.owner)
        actual_name = str(comic.title)
        actual_desc = str(comic.desc)
        self.assertEqual(actual_owner, "testuser1")
        self.assertEqual(actual_name, "Spider Man vs Venom")
        self.assertEqual(
            actual_desc, "The Fight for the City"
        )

    def test_get_comic_list(self):
        url = reverse("comic_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        comics = response.data
        self.assertEqual(len(comics), 1)
        self.assertEqual(comics[0]["title"], "Spider Man vs Venom")


    def test_auth_required(self):
        self.client.logout() 
        url = reverse("comic_list")  
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_only_owner_can_delete_comic(self):
        self.client.logout()
        self.client.login(username="testuser2", password="pass2")
        url = reverse("comic_detail",args=[1])  
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_comic(self):
        self.client.logout()
        self.client.login(username="testuser1", password="pass")    
        url = reverse("comic_detail", args=[1])
        updated_data = {"title": "Superman Dawn of justice", "desc": "two heros clash"}
        response = self.client.patch(url, updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        comic = Comic.objects.get(id=1)
        self.assertEqual(comic.title, updated_data["title"])
        self.assertEqual(comic.desc, updated_data["desc"])

    def test_only_owner_can_delete_comic2(self):
        self.client.logout()
        self.client.login(username="testuser1", password="pass")
        url = reverse("comic_detail",args=[1])  
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    