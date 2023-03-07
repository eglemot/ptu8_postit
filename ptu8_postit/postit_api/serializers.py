from rest_framework import serializers
from . import models


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    post_id = serializers.ReadOnlyField(source='post.id')

    class Meta:
        model = models.Comment
        fields = ('id', 'post_id', 'body', 'user', 'user_id', 'created')


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
