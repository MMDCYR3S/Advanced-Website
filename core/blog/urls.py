from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

# Make a url path for blog views 
urlpatterns = [
    path('fbv-index', views.indexView , name='fbv-index'),
    # path('cbv-index', TemplateView.as_view(template_name='index.html', extra_context={"name": "ali"})),
    path('cbv-index', views.IndexView.as_view(), name='cbv-index'),
]
