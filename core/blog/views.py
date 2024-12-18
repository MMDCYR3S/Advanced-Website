from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView , DetailView
from .models import Post

# Create index view for the main blog page
def indexView(request):
    """
    A function based view to show index page.
    """
    name = 'ali'
    context = {'name': name}
    return render(request, "index.html", context)

# Create custom TemplateView for blog pages
class IndexView(TemplateView):
    """
    This class is responsible for rendering the index
    with TemplateView.
    """
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = "ali"
        context['posts'] = Post.objects.all()
        return context

# ListView of Posts
class PostList(ListView):
    """
    This class is for Posts that uses ListView.
    """
    # model = Post
    # queryset = Post.objects.all()
    paginate_by = 2
    context_object_name = 'posts'
    # ordering = "-id"
    def get_queryset(self):
        posts = Post.objects.filter(status=True).order_by("-id")
        return posts

# DetailView of posts
class PostDetailView(DetailView):
    """
    This class is for detail of a post in blog.
    """
    model = Post