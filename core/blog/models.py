from django.urls import reverse
from django.db import models
from django.contrib.auth import get_user_model

# Getting user model object for author of the post
# User = get_user_model()

# Create Post model for out blog posts
class Post(models.Model):
    """
    In this class, Posts are define for blog application.
    """
    author = models.ForeignKey('accounts.Profile', on_delete=models.CASCADE)
    image = models.ImageField(blank=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    status = models.BooleanField()
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()

    def __str__(self):
        return self.title
    
    def get_snippet(self):
        return self.content[0:5]
    
    def get_absolute_api_url(self):
        return reverse("blog:api-v1:post-detail", kwargs={"pk": self.pk})
    
    
    
# Create Category class for posts of the blog application.
class Category(models.Model):
    """
    This class is used for category. It only has a name
    to define a category. Then, we use foreign key in post
    class to define the category on posts.
    """
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

