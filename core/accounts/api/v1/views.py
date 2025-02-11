from django.shortcuts import get_object_or_404
from mail_templated import EmailMessage

from rest_framework import generics
from rest_framework import status
from .serializers import (
    RegistrationSerializer,
    CustomAuthTokenSerializer, 
    CustomTokenObtainPairSerializer,
    ChangePasswordSerializer,
    ProfileSerializer,
    ActivationResendSerializer,
)
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from django.contrib.auth import get_user_model
from ...models import Profile
from ..utils import EmailThread

import jwt
from jwt.exceptions import(
    ExpiredSignatureError,
    InvalidSignatureError,
    InvalidTokenError,
)
from django.conf import settings

# Creating a user model
User = get_user_model()

# Registration
class RegistrationAPIView(generics.GenericAPIView):
    """ Create a custom api view with generics """
    serializer_class = RegistrationSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = RegistrationSerializer(data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            email = serializer.validated_data["email"]
            data = {
                'email' : email
            }
            user_obj = get_object_or_404(User, email=email)
            token = self.get_tokens_for_user(user_obj)
            email_obj = EmailMessage('email/activation_email.tpl', {'token' : token}, 'admin@admin.com', to=[email])
            EmailThread(email_obj).start()
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
       
    # Manually tokens for user
    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)
        
# Custom token login
class CustomAuthToken(ObtainAuthToken):
    """ Description:
        Login users with token. It gets username and password.
        It can be destroy by logout.
    """
    serializer_class = CustomAuthTokenSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                        context={"request": request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token , created = Token.objects.get_or_create(user=user)
        return Response({
            "token" : token.key,
            "user_id" : user.pk,
            "email" : user.email,
        })

# Logout model
class CustomDiscardAuthToken(APIView):
    """ Description:
        Destroy users with their token.It checks if the a user login
        or not. 
    """
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# Token Pair View
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


# Change password view
class ChangePasswordAPIView(generics.GenericAPIView):
    """ Description:
        Change password with generic api view. Gets object and then checks
        if the password is the same or not.
    """
    model = User
    permission_classes = [IsAuthenticated]
    serializer_class = ChangePasswordSerializer
    
    def get_object(self, queryset=None):
        obj = self.request.user
        return obj
    
    def put(self, request, *args, **kwargs):
        """ Get object and serializer and checks if serializer is valid. """
        self.object = self.get_object()
        serializer = self.get_serializer(data = request.data)
        
        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password" : ["Wrong Password!"]}, status=status.HTTP_400_BAD_REQUEST)
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response({"Detail": "Password change successfully!"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# Profile view
class ProfileAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    
    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, user=self.request.user)
        return obj
    
# Test email
class TestEmailSend(generics.GenericAPIView):
    
    def get(self, request, *args, **kwargs):
        self.email = "amingholami06@gmail.com"
        user_obj = get_object_or_404(User, email=self.email)
        token = self.get_tokens_for_user(user_obj)
        kwargs['email'] = EmailMessage('email/email_sent.tpl', {'token' : token}, 'admin@admin.com', to=[self.email])
        EmailThread(kwargs['email']).start()
        return Response("Email were successfully sent.")
    
    # Manually tokens for user
    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)
        
# Activation class
class ActivationAPIView(APIView):
    """ Activate user with this class """
    def get(self, request, token, *args, **kwargs):
        try:
            token = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            user_id = token.get("user_id")
        except ExpiredSignatureError:
            return Response({"Detail" : "Token has been expired!"}, status=status.HTTP_400_BAD_REQUEST)
        except InvalidSignatureError:
            return Response({"Detail" : "Token is not valid!"}, status=status.HTTP_400_BAD_REQUEST)
        except InvalidTokenError:
            return Response({"Detail" : "Token is not valid!"}, status=status.HTTP_400_BAD_REQUEST)
        user_obj = User.objects.get(pk = user_id)
        user_obj.is_verified = True
        if user_obj.is_verified:
            return Response({"Detail" : "Your account has already been verified!"})
        user_obj.save()
        return Response({"Detail" : "Your account has been verified and activated successfully!"})
    
# resend activation
class ActivationResendAPIView(generics.GenericAPIView):
    """ Resend an activation to activate again """
    serializer_class = ActivationResendSerializer
    def post(self, request, *args, **kwargs):
        serializer = ActivationResendSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_obj = serializer.validated_data["user"]
        token = self.get_tokens_for_user(user_obj)
        kwargs['email'] = EmailMessage('email/activation_email.tpl', {'token' : token}, 'admin@admin.com', to=[user_obj.email])
        EmailThread(kwargs['email']).start()
        return Response({"Detail" : "User activation resend successfully!"}, status=status.HTTP_200_OK)

    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)