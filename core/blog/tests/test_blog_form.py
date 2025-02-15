from django.test import SimpleTestCase, TestCase
from ..forms import PostForm
from ..models import Category
from datetime import datetime

# Create test for post form
class TestPostForm(TestCase):

    def test_post_form_with_valid_data(self):
        category_obj = Category.objects.create(name="Hello")
        form = PostForm(data={
            "title" : "test",
            "content" : "This is a test content",
            "status" : True,
            "category" : category_obj,
            "published_date" : datetime.now()
        }) 
        self.assertTrue(form.is_valid())   
