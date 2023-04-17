from rest_framework.serializers import ModelSerializer, SerializerMethodField

from authentication.serializers import NormalUserDetailSerializer, CommentUserDetailSerializer
from .models import Topic, Comment, Article, BookMark


# Topic
class TopicSerializer(ModelSerializer):
    # related_article_count = SerializerMethodField('get_related_article_count')

    class Meta:
        model = Topic
        fields = '__all__'

    # @classmethod
    # def get_related_article_count(cls, topic):
    #     return Article.objects.filter(related_topics=topic).count()


# Comment
class CreateCommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

    def create(self, validated_data):
        article_id = self.context['request'].data.get('article_id', None)

        if article_id is None or not Article.objects.filter(id=article_id).extra():
            print(f"Article id is none or not found passed article = {article_id}")

        comment = Comment.objects.create(**validated_data)

        article = Article.objects.filter(id=article_id).first()
        article.comments.add(comment.id)

        article.save()
        return comment


class CommentSerializer(ModelSerializer):
    user = CommentUserDetailSerializer()

    class Meta:
        model = Comment
        fields = '__all__'


# Article
class CreateArticleSerializer(ModelSerializer):
    related_topics = TopicSerializer(read_only=True, many=True)
    is_bookmarked = SerializerMethodField('get_is_bookmarked_article')

    class Meta:
        model = Article
        fields = ['id', 'title', 'body', 'writer', 'date_of_publishing', 'cover_image', 'related_topics',
                  'is_bookmarked']

    def get_is_bookmarked_article(self, article):
        user = self.context['request'].user
        return BookMark.objects.filter(user_id=user.id, article_id=article.id).exists()


class ArticleSerializer(ModelSerializer):
    writer = NormalUserDetailSerializer()
    lovers = NormalUserDetailSerializer(many=True)
    related_topics = TopicSerializer(many=True)
    comments = CommentSerializer(many=True)
    is_bookmarked = SerializerMethodField('get_is_bookmarked_article')

    class Meta:
        model = Article
        fields = '__all__'

    def get_is_bookmarked_article(self, article):
        user = self.context['request'].user
        return BookMark.objects.filter(user_id=user.id, article_id=article.id).exists()


class CreateArticleLoveSerializer(ModelSerializer):
    writer = NormalUserDetailSerializer(read_only=True)
    lovers = NormalUserDetailSerializer(many=True, read_only=True)
    related_topics = TopicSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = '__all__'

        extra_kwargs = {
            'title': {'read_only': True},
            'body': {'read_only': True},
            'cover_image': {'read_only': True},
            'date_of_publishing': {'read_only': True},
            'writer': {'read_only': True},
            'comments': {'read_only': True},
            'related_topics': {'read_only': True},
        }


class UpdateArticleRelatedTopicsSerializer(ModelSerializer):
    writer = NormalUserDetailSerializer(read_only=True)
    lovers = NormalUserDetailSerializer(many=True, read_only=True)
    related_topics = TopicSerializer(many=True, write_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = '__all__'

        extra_kwargs = {
            'title': {'read_only': True},
            'body': {'read_only': True},
            'cover_image': {'read_only': True},
            'date_of_publishing': {'read_only': True},
            'writer': {'read_only': True},
            'comments': {'read_only': True},
            'lovers': {'read_only': True},
            'related_topics': {'write_only': True},
        }


# Bookmark
class CreateBookmarkSerializer(ModelSerializer):
    class Meta:
        model = BookMark
        fields = ['id', 'article']

    def create(self, validated_data):
        user = self.context['request'].user
        return BookMark.objects.create(user_id=user.id, **validated_data)


class BookmarkSerializer(ModelSerializer):
    article = ArticleSerializer()

    class Meta:
        model = BookMark
        fields = ['id', 'article']
