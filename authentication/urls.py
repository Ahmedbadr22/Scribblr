from django.urls import path
from .views import (LoginView, UserCreationAPIView, SuperuserCreationAPIView, CreateCountryAPIView,
                    CreateSocialLinkAPIView, CreateSocialPlatformAPIView, ListCountriesAPIView,
                    ListSocialLinksAPIView, ListSocialPlatformsAPIView, RetrieveCountryAPIView,
                    RetrieveSocialLinkAPIView, RetrieveSocialPlatformAPIView, DeleteCountryAPIView,
                    DeleteSocialLinkPIView, DeleteSocialPlatformAPIView, UpdateUserAPIView, CreateFollowerAPIView)

urlpatterns = [
    # Login
    path('login', LoginView.as_view()),
    path('create-user', UserCreationAPIView.as_view()),
    path('create-super-user', SuperuserCreationAPIView.as_view()),
    path('update-user/<int:id>', UpdateUserAPIView.as_view()),
    # follower
    path('create-user-follower', CreateFollowerAPIView.as_view()),
    # Country
    path('create-country', CreateCountryAPIView.as_view()),
    path('list-countries', ListCountriesAPIView.as_view()),
    path('get-country/<int:id>', RetrieveCountryAPIView.as_view()),
    path('delete-country/<int:id>', DeleteCountryAPIView.as_view()),
    # Social Platform
    path('create-social-platform', CreateSocialPlatformAPIView.as_view()),
    path('list-social-platforms', ListSocialPlatformsAPIView.as_view()),
    path('get-social-platform/<int:id>', RetrieveSocialPlatformAPIView.as_view()),
    path('delete-social-platform/<int:id>', DeleteSocialPlatformAPIView.as_view()),
    # Social Links
    path('create-social-link', CreateSocialLinkAPIView.as_view()),
    path('list-social-links', ListSocialLinksAPIView.as_view()),
    path('get-social-link/<int:id>', RetrieveSocialLinkAPIView.as_view()),
    path('delete-social-link/<int:id>', DeleteSocialLinkPIView.as_view()),
]
