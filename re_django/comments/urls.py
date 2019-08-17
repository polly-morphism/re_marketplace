from rest_framework import routers
from comments.views import RatingViewSet
from django.conf.urls import url, include

router = routers.DefaultRouter()
router.register(r'ratings', RatingViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    ]
