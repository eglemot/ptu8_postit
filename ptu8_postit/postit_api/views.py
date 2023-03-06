from rest_framework import generics
from . import models, serializers


class PostList(generics.ListCreateAPIView):
    serializer_class = serializers.PostSerializer
    queryset = models.Post.objects.all()
