# from django.conf.urls import url, include
from rest_framework import routers
from api.views import SellerViewSet
from django.conf.urls import url, include

router = routers.DefaultRouter()
router.register(r'users', SellerViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    ]
