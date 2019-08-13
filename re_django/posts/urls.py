from rest_framework import routers
from posts.views import SellPostViewSet, RentOutPostViewSet, RentPostViewSet, BuyPostViewSet
from django.conf.urls import url, include

router = routers.DefaultRouter()
router.register(r'sellposts', SellPostViewSet)
router.register(r'rentoutposts', RentOutPostViewSet)
router.register(r'rentposts', RentPostViewSet)
router.register(r'buyposts', BuyPostViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    ]
