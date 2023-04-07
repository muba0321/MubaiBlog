from rest_framework import serializers
from .models import User, Article, Comment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'nickname', 'is_author', 'avatar']


class ArticleSerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'author', 'created_time', 'updated_time', 'read_num']


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    article = ArticleSerializer()

    class Meta:
        model = Comment
        fields = ['id', 'content', 'user', 'article', 'created_time', 'updated_time']
