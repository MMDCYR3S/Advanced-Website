from django import forms
from .models import Post


# Create form to make posts
class PostForm(forms.ModelForm):
    """
    This class has used for for creating posts. It gets
    model(like Post in the bottom) to recognize the process
    it should do. Then, you can choose which fields you want
    to add to create a post.
    """

    class Meta:
        model = Post
        fields = ["author", "title", "content", "status", "category", "published_date"]
