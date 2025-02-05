from .. import views
from django.urls import path, include
from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
# from rest_framework.authtoken.views import ObtainAuthToken

# Make a url path for blog 
urlpatterns = [
    # Register, login and logout with token
    path("registration/", views.RegistrationAPIView.as_view(), name="registration"),
    path("token/login/", views.CustomAuthToken.as_view(), name="token-login"),
    path("token/logout/", views.CustomDiscardAuthToken.as_view(), name="token-logout"),
    
    # Change password
    path("change-password/", views.ChangePasswordAPIView.as_view(), name="change-password"),
    
    # JWT(Json Web Token)
    path("jwt/create/", views.CustomTokenObtainPairView.as_view(), name="jwt-create"),
    path("jwt/refresh/", TokenRefreshView.as_view(), name="jwt-refresh"),
    path("jwt/verify/", TokenVerifyView.as_view(), name="jwt-verify"),
    
    # Activation and resend activation
    path('test-email/', views.TestEmailSend.as_view(), name="test-email")
    # path('activation/confirm/', )
]