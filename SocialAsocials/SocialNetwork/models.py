import uuid
from django.db import models


# Create your models here.
class User(models.Model):
    # Should have unique id.
    created = models.DateField(auto_created=True, auto_now=True)
    username = models.CharField(max_length=20, unique=True, editable=True)
    first_name = models.CharField(max_length=25, blank=True)
    last_name = models.CharField(max_length=25, blank=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=30)
    telephone = models.CharField(max_length=100, blank=True, null=True)
    birth = models.DateField(blank=True, null=True)
    about_me = models.CharField(max_length=255, blank=True, null=True)
    current_status = models.CharField(max_length=255, blank=True, null=True)
    amount_friends = models.PositiveIntegerField(editable=False, auto_created=True, default=0)

    def __str__(self):
        return self.username


class Post(models.Model):
    # Should link post_id with creator_id (user).
    creator_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_created=True)
    content = models.CharField(max_length=1255)
    likes = models.IntegerField(default=0)
    amount_comments = models.IntegerField(default=0)

    def __str__(self):
        return "By:{}, On: {}, 10 Content: {}"


class Comment(models.Model):
    # Should link a creator_id to comment_id to a post_id,
    creator_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_created=True)
    content = models.CharField(max_length=400)
    likes = models.PositiveIntegerField(default=0)
