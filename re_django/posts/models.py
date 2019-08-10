from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.utils import timezone

from phonenumber_field.modelfields import PhoneNumberField


class SellPost(models.Model):

    HOUSE = 'H'
    FLAT = 'F'
    OTHER = 'O'
    ROOM = 'R'

    RE_TYPE_CHOICES = [
        (HOUSE, 'House'),
        (FLAT, 'Flat'),
        (ROOM, 'Room'),
        (OTHER, 'Other'),
        ]

    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    info = models.TextField(blank=True,)
    photo = models.ImageField(blank=True,)
    country = models.CharField(max_length=50, blank=False,)
    city = models.CharField(max_length=50, blank=False,)
    district = models.CharField(max_length=50, blank=False,)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    size = models.PositiveSmallIntegerField()
    type = models.CharField(
        max_length=1,
        choices=RE_TYPE_CHOICES,
        default=FLAT,
    )

    type_other = models.CharField(max_length=50, blank=True,)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
