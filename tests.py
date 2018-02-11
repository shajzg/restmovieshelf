"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""
#from django.test import TestCase
#
#class SimpleTest(TestCase):
#    def test_basic_addition(self):
#        """
#        Tests that 1 + 1 always equals 2.
#        """
#        self.failUnlessEqual(1 + 1, 2)
#
#__test__ = {"doctest": """
#Another way to test that 1 + 1 is equal to 2.
#
#>>> 1 + 1 == 2
#True
#"""}

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from pymovieshelf.models import Movie

from rest_framework_jwt.settings import api_settings
from django.contrib.auth import get_user_model

from rest_framework.reverse import reverse as api_reverse

payload_handler = api_settings.JWT_PAYLOAD_HANDLER
encode_handler  = api_settings.JWT_ENCODE_HANDLER

User = get_user_model()

class MovieTests(APITestCase):
    def setUp(self):
        user_obj = User(username='testuser',email='test@test.com')
        user_obj.set_password("testpassword")
        user_obj.save()

    def test_user_login(self):
        data = {
            'username': 'testuser',
            'password': 'testpassword'
        }
        url = api_reverse("api-login")
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)



    def test_create_movie(self):
        """
        Ensure we can create a new movie.
        """
        data = {
            'username': 'testuser',
            'password': 'testpassword'
        }
        url = api_reverse("api-login")
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        token = response.data.get("token")
        url = reverse('movie-create')
        data = {"title":"The Matrix","chinesetitle":"hhe","director":"Lana Wachowski, Lilly Wachowski","rated":0,"year":"1999","genres":"Action, Sci-Fi","summary":"A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.","fmt":"2","length":"136 min","rating":"8.7","production":"Warner Bros. Pictures","sn":"sdfs","url":"http://www.whatisthematrix.com","img":"https://images-na.ssl-images-amazon.com/images/M/MV5BNzQzOTk3OTAtNDQ0Zi00ZTVkLWI0MTEtMDllZjNkYzNjNTc4L2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SX300.jpg"}
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Movie.objects.count(), 1)
        self.assertEqual(Movie.objects.get().fmt, 'DVD')

    def test_list_movies(self):
        url = api_reverse("movie-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
