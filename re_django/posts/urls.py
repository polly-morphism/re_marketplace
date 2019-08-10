from rest_framework import routers
from posts.views import SellPostViewSet
from django.conf.urls import url, include

router = routers.DefaultRouter()
router.register(r'posts', SellPostViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    ]
