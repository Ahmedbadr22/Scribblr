from .models import User, Country, SocialLink, SocialPlatform
from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView, RetrieveAPIView, UpdateAPIView
from .serializers import (SuperuserCreationSerializer, UserCreationSerializer, TokenObtainPairSerializer,
                          CountrySerializer, CreateSocialLinkSerializer, SocialLinkSerializer, SocialPlatformSerializer,
                          UserUpdateSerializer, CreateFollowerSerializer)

from rest_framework_simplejwt.views import TokenObtainPairView


class SuperuserCreationAPIView(CreateAPIView):
    """
    Create Superuser Api View
    """
    queryset = User.objects.all()
    serializer_class = SuperuserCreationSerializer


# Normal user creation
class UserCreationAPIView(CreateAPIView):
    """
    Create Normal User Api View
    """
    queryset = User.objects.all()
    serializer_class = UserCreationSerializer


class UpdateUserAPIView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    lookup_field = 'id'


class LoginView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer


# Followers
class CreateFollowerAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateFollowerSerializer


# Country
class CreateCountryAPIView(CreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class ListCountriesAPIView(ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class RetrieveCountryAPIView(RetrieveAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    lookup_field = 'id'


class DeleteCountryAPIView(DestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    lookup_field = 'id'


# Social Platforms
class CreateSocialPlatformAPIView(CreateAPIView):
    queryset = SocialPlatform.objects.all()
    serializer_class = SocialPlatformSerializer


class ListSocialPlatformsAPIView(ListAPIView):
    queryset = SocialPlatform.objects.all()
    serializer_class = SocialPlatformSerializer


class RetrieveSocialPlatformAPIView(RetrieveAPIView):
    queryset = SocialPlatform.objects.all()
    serializer_class = SocialPlatformSerializer
    lookup_field = 'id'


class DeleteSocialPlatformAPIView(DestroyAPIView):
    queryset = SocialPlatform.objects.all()
    serializer_class = SocialPlatformSerializer
    lookup_field = 'id'


# Social Links
class CreateSocialLinkAPIView(CreateAPIView):
    queryset = SocialLink.objects.all()
    serializer_class = CreateSocialLinkSerializer


class ListSocialLinksAPIView(ListAPIView):
    queryset = SocialLink.objects.all()
    serializer_class = SocialLinkSerializer


class RetrieveSocialLinkAPIView(RetrieveAPIView):
    queryset = SocialLink.objects.all()
    serializer_class = SocialLinkSerializer
    lookup_field = 'id'


class DeleteSocialLinkPIView(DestroyAPIView):
    queryset = SocialLink.objects.all()
    serializer_class = SocialLinkSerializer
    lookup_field = 'id'
