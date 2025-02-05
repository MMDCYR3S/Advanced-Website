from .. import views
from django.urls import path, include
# from rest_framework.authtoken.views import ObtainAuthToken

# Make a url path for blog 
urlpatterns = [
    # Profile
    path("", views.ProfileAPIView.as_view(), name="profile"),
]