from django.shortcuts import render
from django.views.generic.base import TemplateView
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

