from rest_framework import viewsets
from posts.models import SellPost, RentOutPost
from posts.serializers import SellPostSerializer, RentOutPostSerializer


class SellPostViewSet(viewsets.ModelViewSet):
    queryset = SellPost.objects.all()
    serializer_class = SellPostSerializer

class RentOutPostViewSet(viewsets.ModelViewSet):
    queryset = RentOutPost.objects.all()
    serializer_class = RentOutPostSerializer
