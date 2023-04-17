from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db.models import (
    EmailField,
    ImageField,
    CharField,
    DateTimeField,
    DateField,
    BooleanField,
    Model,
    ForeignKey,
    CASCADE,
    FileField,
    ManyToManyField,
    TextField,
    DO_NOTHING,
)

from .managers import UserManager


class SocialPlatform(Model):
    name = CharField(max_length=255, unique=True)
    icon = FileField(upload_to="social-platform/")


class SocialLink(Model):
    platform = ForeignKey(SocialPlatform, on_delete=CASCADE)
    link = CharField(max_length=2000, unique=True)


class Country(Model):
    name = CharField(max_length=255)
    abbreviation = CharField(max_length=255)
    flag_image = ImageField(upload_to='country/flags/')


class User(AbstractBaseUser, PermissionsMixin):
    username = CharField(max_length=255, unique=True)
    email = EmailField(unique=True)
    phone_number = CharField(max_length=11, null=True, blank=True)
    profile_image = ImageField(upload_to='user-profile/', null=True, blank=True)
    full_name = CharField(max_length=255)
    date_of_join = DateTimeField(auto_now_add=True)
    birth_date = DateField()
    gender = BooleanField(default=True)
    about = TextField()
    address = CharField(max_length=500, null=True, blank=True)
    website_link = CharField(max_length=500, null=True, blank=True)
    country = ForeignKey(Country, on_delete=DO_NOTHING, null=True, blank=True)
    social_links = ManyToManyField(SocialLink)
    is_active = BooleanField(default=True)
    is_superuser = BooleanField(default=False)
    is_staff = BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class Follower(Model):
    user_writer = ForeignKey(User, on_delete=CASCADE, related_name='user_writer')
    user_follower = ForeignKey(User, on_delete=CASCADE, related_name='user_follower')
