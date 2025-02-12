from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

app_name = "api-v1"

# Creating router
router = DefaultRouter()
router.register("post", views.PostModelViewSet, basename="post")
router.register("category", views.CategoryModelViewSet, basename="category")
urlpatterns = router.urls

# Make a url path for blog
# urlpatterns = [
#     # path('post/', views.PostList.as_view(), name="post-list"),
#     # path('post/<int:pk>/', views.PostDetail.as_view(), name="post-detail"),
#     # path('post/<int:id>/', views.post_detail, name="post-detail"),

#     path('post/', views.PostViewSet.as_view({'get': 'list', 'post': 'create'}), name="post-list"),
#     path('post/<int:pk>/', views.PostViewSet.as_view({'get': 'retrieve', 'put': 'update',
#         'patch': 'partial_update', 'delete': 'destroy'}), name='post-detail'),
#     path('', include(router.urls)),

# ]
