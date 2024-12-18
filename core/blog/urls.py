from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

app_name = "blog"

# Make a url path for blog views 
urlpatterns = [
    # path('fbv-index', views.indexView , name='fbv-index'),
    # path('cbv-index', views.IndexView.as_view(), name='cbv-index'),
    path('post/', views.PostList.as_view(), name="post-list"),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name="post-detail"),
]
