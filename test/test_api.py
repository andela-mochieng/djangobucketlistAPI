from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from api.models import BucketList, BucketListItem
import json
from faker import Factory

fake = Factory.create()

class UserTests(APITestCase):
    """
    Tests to do with user registration and login
    """
    def setUp(self):
        self.username = fake.name().replace(' ', '')
        self.email = fake.email()
        self.password = fake.password()
        self.user = User.objects.create_user(
            username=self.username, email=self.email, password=self.password)

    def test_user_registers_successfully(self):
        """Tests that a user is able to register with correct details"""

        url = reverse('register')
        username = fake.name().replace(' ', '')
        data = {"username": username, "email":fake.email(), "password":fake.password()}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data.get('username'), username)

    def test_user_creation_fails_when_same_user_registers(self):
        """
        Test whether user creation fails when same user tries to re-register
        """
        url = reverse('register')
        data = {'username': self.username, 'email':self.email, 'password':self.password}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotEqual(response.data.get('username'), "A user with that username already exists.")


    def test_users_can_login_when_they_provide_correct_info(self):
        """Tests user can login when they provide right info"""
        url = reverse('login')
        data = {'username': self.username, 'password':self.password}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("token", response.data)


    def test_users_can_not_login_when_they_provide_wrong_info(self):
        """Tests user can't login when he provides wrong info"""
        url = reverse('login')
        self.username = fake.name()
        data = {'username': self.username, 'password':self.password}
        response = self.client.post(url, data)
        self.assertNotIn("token", response.data)
        self.assertIn(
            "Unable to login with provided credentials.",
            response.data.get('non_field_errors'))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class BucketListTests(APITestCase):
    """
    Tests to do with BucketList creation  and deletion
    """
    def setUp(self):
        """Set up data specific to the test cases for bucketlist"""
        # bucketlist specific details
        self.list_name = fake.first_name()
        # create a user
        self.username = fake.name().replace(' ', '')
        self.password = fake.password();
        self.user = User.objects.create_user(
            username=self.username,  password=self.password)

        self.bucketlist = BucketList.objects.create(list_name=self.list_name, creator=self.user)

        # login a user
        url = reverse('login')
        data = {'username': self.username, 'password':self.password}
        self.response = self.client.post(url, data)
        self.token = self.response.data.get('token')
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + self.token)

    def tearDown(self):
        """Delete the user modal after use"""
        del self.user
        del self.bucketlist
        del self.token
        del self.response

    def test_bucketlist_creation_succeeds_when_right_info_is_provided(self):
        """Tests whether bucketlist gets created when he provides the right info"""
        self.list_name = fake.first_name()
        data = {'list_name': self.list_name}
        url = reverse('blists')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data.get('list_name'), self.list_name)


    def test_bucketlist_creation_fails_when_wrong_info_is_provided(self):
        """Tests whether bucketlist isn't created when he provides the right info"""
        data = {'list_name': self.list_name}
        url = reverse('blists')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotEqual(response.data.get('list_name'), self.list_name)


    def test_bucketlist_deletion_succeeds(self):
        """Tests whether bucketlist gets deleted """
        bucketlist = BucketList.objects.get(list_name=self.list_name)
        url = "/api/v.1/bucketlists/{}/".format(bucketlist.id)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

   
    def tearDown(self):
        """Delete user modal after use"""
        del self.user
