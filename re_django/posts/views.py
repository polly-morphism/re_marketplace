from rest_framework import viewsets
from posts.models import SellPost
from posts.serializers import SellPostSerializer


class SellPostViewSet(viewsets.ModelViewSet):
    queryset = SellPost.objects.all()
    serializer_class = SellPostSerializer
