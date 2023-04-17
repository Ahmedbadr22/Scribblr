from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from .models import Article, Topic, Comment, BookMark
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializer import (TopicSerializer, CreateCommentSerializer, CreateBookmarkSerializer,
                         CreateArticleSerializer, CreateArticleLoveSerializer, BookmarkSerializer,
                         ArticleSerializer, UpdateArticleRelatedTopicsSerializer)


# Topic
class CreateTopicAPIView(CreateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class ListTopicsAPIView(ListAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class RetrieveTopicAPIView(RetrieveAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    lookup_field = 'id'


class DeleteTopicAPIView(DestroyAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    lookup_field = 'id'


class UpdateTopicAPIView(UpdateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    lookup_field = 'id'


# Comment
class CreateCommentAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CreateCommentSerializer


# Article
class CreateArticleAPIView(CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = CreateArticleSerializer


class CreateArticleLoveAPIView(UpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = CreateArticleLoveSerializer
    lookup_field = 'id'


class UpdateArticleRelatedTopicsAPIView(UpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = UpdateArticleRelatedTopicsSerializer
    lookup_field = 'id'


class ListArticlesAPIView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]


class RetrieveArticleAPIView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'id'


class DeleteArticleAPIView(DestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'id'


class UpdateArticleAPIView(UpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'id'


# Bookmark
class CreateBookMarkAPIView(CreateAPIView):
    queryset = BookMark.objects.all()
    serializer_class = CreateBookmarkSerializer
    permission_classes = [IsAuthenticated]


class ListBookmarkArticlesAPIView(ListAPIView):
    queryset = BookMark.objects.all()
    serializer_class = BookmarkSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return self.queryset.filter(user_id=user.id)


class RetrieveBookMarkArticleByIdAPIView(RetrieveAPIView):
    queryset = BookMark.objects.all()
    serializer_class = BookmarkSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        user = self.request.user
        bookmark_id = self.kwargs[self.lookup_field]
        print(id)
        return self.queryset.filter(user_id=user.id, id=bookmark_id)


class DeleteBookMarkArticleByIdAPIView(DestroyAPIView):
    queryset = BookMark.objects.all()
    serializer_class = BookmarkSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        user = self.request.user
        bookmark_id = self.kwargs[self.lookup_field]
        print(id)
        return self.queryset.filter(user_id=user.id, id=bookmark_id)
