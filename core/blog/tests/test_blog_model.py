from django.test import TestCase
from ..models import Post, Category
from django.contrib.auth import get_user_model
from accounts.models import User, Profile

from datetime import datetime

# create test model class
class TestPostModel(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(email="test@test.com", password="@Ab1234567")
        self.profile = Profile.objects.create(
            user = self.user,
            first_name = "mamad",
            last_name = "gh",
            description = "test",
        )
    
    def test_create_post_with_valid_data(self):
        post = Post(
            author = self.profile,
            image = None,
            title = "test",
            content = "This is a test content.",
            status = True,
            category = None,
            created_date = datetime.now(),
            updated_date = datetime.today(),
            published_date = datetime.now()
        )
        self.assertFalse(Post.objects.filter(pk=post.id).exists())