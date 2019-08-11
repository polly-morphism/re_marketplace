from rest_framework import routers
from posts.views import SellPostViewSet, RentOutPostViewSet
from django.conf.urls import url, include

router = routers.DefaultRouter()
router.register(r'sellposts', SellPostViewSet)
router.register(r'rentoutposts', RentOutPostViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    ]
