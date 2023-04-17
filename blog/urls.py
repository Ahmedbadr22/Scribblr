from django.urls import path
from .views import (CreateTopicAPIView, CreateArticleAPIView, CreateCommentAPIView, ListTopicsAPIView,
                    ListArticlesAPIView, CreateArticleLoveAPIView, UpdateArticleRelatedTopicsAPIView,
                    CreateBookMarkAPIView, ListBookmarkArticlesAPIView, RetrieveBookMarkArticleByIdAPIView,
                    DeleteBookMarkArticleByIdAPIView)

urlpatterns = [
    # Topic
    path('create-topic', CreateTopicAPIView.as_view()),
    path('list-topics', ListTopicsAPIView.as_view()),
    # Comment
    # Article
    path('create-article', CreateArticleAPIView.as_view()),
    path('create-article-comment', CreateCommentAPIView.as_view()),
    path('create-article-love/<int:id>', CreateArticleLoveAPIView.as_view()),
    path('create-article-topic/<int:id>', UpdateArticleRelatedTopicsAPIView.as_view()),
    path('list-articles', ListArticlesAPIView.as_view()),
    # bookmark
    path('create-bookmark', CreateBookMarkAPIView.as_view()),
    path('list-user-bookmarks', ListBookmarkArticlesAPIView.as_view()),
    path('get-user-bookmark/<int:id>', RetrieveBookMarkArticleByIdAPIView.as_view()),
    path('delete-user-bookmark/<int:id>', DeleteBookMarkArticleByIdAPIView.as_view()),

]
