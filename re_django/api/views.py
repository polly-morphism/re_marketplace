from rest_framework import viewsets
from api.models import Seller
from api.serializers import SellerSerializer


class SellerViewSet(viewsets.ModelViewSet):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
