from django.contrib.auth import get_user_model
from rest_framework import serializers
from . import models


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    post_id = serializers.ReadOnlyField(source='post.id')
    like_count = serializers.SerializerMethodField()

    def get_like_count(self, obj):
        return models.CommentLike.objects.filter(comment=obj).count()

    class Meta:
        model = models.Comment
        fields = ('id', 'post_id', 'body', 'user', 'user_id', 'created', 'like_count')


class PostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    # comments = CommentSerializer(many=True)
    # comments = serializers.StringRelatedField(many=True, read_only=True)
    comment_count = serializers.SerializerMethodField()
    like_count = serializers.SerializerMethodField()

    def get_comment_count(self, obj):
        return models.Comment.objects.filter(post=obj).count()

    def get_like_count(self, obj):
        return models.PostLike.objects.filter(post=obj).count()

    class Meta:
        model = models.Post
        fields = (
            'id', 'title', 'body', 'user', 'user_id', 'comment_count', 
            'like_count', 'created', 'image',
        )


class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PostLike
        fields = ('id', )


class CommentLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CommentLike
        fields = ('id', )
