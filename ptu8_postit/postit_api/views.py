from rest_framework import generics
from . import models, serializers


class PostList(generics.ListAPIView):
    serializer_class = serializers.PostSerializer
    queryset = models.Post.objects.all()
