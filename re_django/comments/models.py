from django.db import models
from django.conf import settings
from django.utils import timezone


class Rating(models.Model):

    RATING_CHOICES = (
    (5, '5'),
    (4, '4'),
    (3, '3'),
    (2, '2'),
    (1, '1'),
    )

    from_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="from+", on_delete=models.CASCADE)
    user_to = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="to+", on_delete=models.CASCADE)
    text = models.TextField(blank=True,)
    rating = models.PositiveIntegerField(choices=RATING_CHOICES, default= 5)
    created_date = models.DateTimeField(default=timezone.now)
