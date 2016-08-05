from django.test import TestCase
from django.db import IntegrityError

from faker import Factory
from django.contrib.auth.models import User
from api.models import BucketList, BucketListItem

fake = Factory.create()


class UserTests(TestCase):
    """Tests for User Modal"""

    def setUp(self):
        """Setting up of the modal for use"""
        self.username = fake.name().replace(' ', '')
        self.password = fake.password()
        self.user = User.objects.create_user(
            username=self.username,  password=self.password)

    def tearDown(self):
        """Delete the user modal after use"""
        del self.user

    def test_super_user_created(self):
        """Test the creation of a user"""
        self.assertIsInstance(self.user, User)

    def test_super_user_creation_fails(self):
        """Test the creation of a user fails"""
        try:
            self.user = User.objects.create_user(
                username=self.username, password=self.password)
        except IntegrityError as e:
            self.assertIn("column username is not unique", e.message)


class BucketListTests(TestCase):
    """Test class for a BucketList Model"""

    def setUp(self):
        """Environment test setup for the model"""
        self.username = fake.user_name()
        self.password = fake.password()
        self.user = User.objects.create_user(
            username=self.username,  password=self.password, is_superuser=True)
        self.list_name = fake.first_name()
        self.bucketlist = BucketList(list_name=self.list_name, creator=self.user)

    def test_bucket_list_created(self):
        """Test bucketlist gets created"""
        self.assertIsInstance(self.bucketlist, BucketList)

    def test_str_method(self):
        """Test string representation of a bucketlist"""
        self.assertIn(str(self.bucketlist),
                         "BucketList : {}".format(self.list_name))


class BucketListItemTests(TestCase):
    """Class containing tests for a BucketList-Item Modal"""

    def setUp(self):
        """setup method for creating test enviroment of the modal"""
        self.item_name = fake.first_name()
        self.username = fake.first_name()
        self.password = fake.password()
        self.user = User.objects.create_user(
            username=self.username,  password=self.password, is_superuser=True)
        self.list_name = fake.first_name()
        self.bucketlist = BucketList(list_name=self.list_name, creator=self.user)
        self.b_item = BucketListItem(
            item_name=self.item_name, bucketlist=self.bucketlist)

    def test_bucket_list_item_created(self):
        """Test creation of item in a bucketlist"""
        self.assertIsInstance(self.b_item, BucketListItem)

    def test_str_method(self):
        """test string representation of a BucketListItem modal"""
        self.assertIn(str(self.b_item),
                         "Item : {}".format(self.item_name))