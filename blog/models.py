from django.db.models import (
    Model,
    CharField,
    TextField,
    ImageField,
    DateTimeField,
    ManyToManyField,
    ForeignKey,
    CASCADE
)


class Topic(Model):
    name = TextField()
    cover_image = ImageField(upload_to='topic/cover_image/')


class Comment(Model):
    user = ForeignKey("authentication.User", on_delete=CASCADE)
    comment = TextField()
    date_of_commenting = DateTimeField(auto_now_add=True)


class Article(Model):
    title = CharField(max_length=255, unique=True)
    body = TextField()
    cover_image = ImageField(upload_to='blog/article/image')
    date_of_publishing = DateTimeField(auto_now_add=True)
    writer = ForeignKey("authentication.User", on_delete=CASCADE)
    lovers = ManyToManyField("authentication.User", related_name='article_lovers_user')
    comments = ManyToManyField(Comment)
    related_topics = ManyToManyField(Topic)


class BookMark(Model):
    article = ForeignKey(Article, on_delete=CASCADE)
    user = ForeignKey("authentication.User", on_delete=CASCADE)
