from django.urls import path
from . import views

app_name = "api-v1"

# Make a url path for blog views 
urlpatterns = [
    path('post/', views.PostList.as_view(), name="post-list"),
    path('post/<int:id>/', views.PostDetail.as_view(), name="post-detail"),  
    # path('post/<int:id>/', views.post_detail, name="post-detail"),  
]
