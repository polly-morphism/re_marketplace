from rest_framework import viewsets
from posts.models import SellPost, RentOutPost, RentPost, BuyPost
from posts.serializers import SellPostSerializer, RentOutPostSerializer, RentPostSerializer, BuyPostSerializer


class SellPostViewSet(viewsets.ModelViewSet):
    queryset = SellPost.objects.all()
    serializer_class = SellPostSerializer

class RentOutPostViewSet(viewsets.ModelViewSet):
    queryset = RentOutPost.objects.all()
    serializer_class = RentOutPostSerializer

class RentPostViewSet(viewsets.ModelViewSet):
    queryset = RentPost.objects.all()
    serializer_class = RentPostSerializer

class BuyPostViewSet(viewsets.ModelViewSet):
    queryset = BuyPost.objects.all()
    serializer_class = BuyPostSerializer
