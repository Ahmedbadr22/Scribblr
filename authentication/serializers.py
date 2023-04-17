from rest_framework.serializers import ModelSerializer, SerializerMethodField
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User, Country, SocialLink, SocialPlatform, Follower


class TokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['user_id'] = user.id
        token['full_name'] = user.full_name
        token['gender'] = user.gender
        # ...

        return token


class SuperuserCreationSerializer(ModelSerializer):
    """
    Superuser Creation Serializer by 'email', 'password', 'first_name', 'last_name'
    """

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'full_name', 'gender']

        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = User.objects.create_superuser(**validated_data)
        user.save()
        return user


class UserCreationSerializer(ModelSerializer):
    """
    Normal User Creation Serializer by 'email', 'password', 'first_name', 'last_name'
    """

    class Meta:
        model = User
        fields = ['profile_image', 'username', 'email', 'password',
                  'full_name', 'gender', 'country', 'birth_date', 'phone_number']

        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.save()
        return user


class CreateFollowerSerializer(ModelSerializer):
    class Meta:
        model = Follower
        fields = '__all__'


class UserUpdateSerializer(ModelSerializer):
    """
    Normal User Update Serializer
    """

    class Meta:
        model = User
        fields = ['username', 'email', 'full_name', 'gender', 'country', 'website_link', 'about', 'address',
                  'social_links']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.save()
        return user


# Country
class CountrySerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


# Social Platform
class SocialPlatformSerializer(ModelSerializer):
    class Meta:
        model = SocialPlatform
        fields = '__all__'


# Social Links
class CreateSocialLinkSerializer(ModelSerializer):
    class Meta:
        model = SocialLink
        fields = '__all__'


class SocialLinkSerializer(ModelSerializer):
    platform = SocialPlatformSerializer()

    class Meta:
        model = SocialLink
        fields = '__all__'


# User
class NormalUserDetailSerializer(ModelSerializer):
    country = CountrySerializer()
    social_links = SocialLinkSerializer(many=True)
    followers = SerializerMethodField('get_user_writer_followers')

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'full_name', 'gender', 'address', 'country', 'social_links',
                  'website_link', 'profile_image', 'about', 'followers']

    @classmethod
    def get_user_writer_followers(cls, user):
        followers = Follower.objects.filter(user_writer_id=user.id)
        serializer = CreateFollowerSerializer(followers, many=True)
        return serializer.data


class CommentUserDetailSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'full_name', 'profile_image']
