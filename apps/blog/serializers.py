from django.contrib.auth.models import User
from rest_framework import serializers

from apps.blog.models import Category, Blog, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'


class BlogItemSerializer(serializers.ModelSerializer):
    comment_list = CommentSerializer(source='comment_set', read_only=True, many=True)

    class Meta:
        model = Blog
        fields = '__all__'
