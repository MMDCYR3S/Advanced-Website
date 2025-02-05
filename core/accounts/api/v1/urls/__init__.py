from django.urls import path, include

# Make pre-urls
urlpatterns = [
    path("", include("accounts.api.v1.urls.accounts")),
    path("", include("accounts.api.v1.urls.profiles")),
]