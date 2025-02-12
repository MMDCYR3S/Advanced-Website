from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


# Create index view for the main blog page
def indexView(request):
    """
    A function based view to show index page.
    """
    name = "ali"
    context = {"name": name}
    return render(request, "index.html", context)


# Create custom TemplateView for blog pages
class IndexView(TemplateView):
    """
    This class is responsible for rendering the index
    with TemplateView.
    """

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "ali"
        context["posts"] = Post.objects.all()
        return context


# ListView of Posts
class PostList(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    """
    This class is for Posts that uses ListView.
    """

    # model = Post
    # queryset = Post.objects.all()
    permission_required = "blog.view_post"
    paginate_by = 2
    context_object_name = "posts"

    # ordering = "-id"
    def get_queryset(self):
        posts = Post.objects.filter(status=True).order_by("-id")
        return posts

# DetailView of posts
class PostDetailView(PermissionRequiredMixin, LoginRequiredMixin, DetailView):
    """
    This class is for detail of a post in blog.
    """
    model = Post
    permission_required = "blog.view_post"
"""
# FormView
class PostCreateView(FormView):
    template_name = "contact.html"
    form_class = PostForm
    success_url = "/blog/post/"
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
"""

# CreateView for making new posts
class PostCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    
    permission_required = "blog.create_post"
    model = Post
    fields = ["title", "content", "status", "category", "published_date"]
    success_url = "/blog/post/"
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# UpdateView for editing posts
class PostEditView(UpdateView):
    
    """
    This class is used for editing posts.
    """
    model = Post
    form_class = PostForm
    success_url = "/blog/post/"

# DeleteView for delete posts in blog
class PostDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    
    """
    This class is used for deleting posts. It gets model
    to recognize it. Then, gets a url to get back to the page
    you wanna go.
    """
    model = Post
    success_url = "/blog/post/"
