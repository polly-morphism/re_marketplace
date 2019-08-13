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
    price = models.PositiveIntegerField(default = 0)
    type = models.CharField(
        max_length=1,
        choices=RE_TYPE_CHOICES,
        default=FLAT,
    )

    type_other = models.CharField(max_length=50, blank=True,)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

class RentOutPost(models.Model):

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

    DAILY = 'D'
    MONTHLY = 'M'
    YEARLY = 'Y'

    RENT_TYPE_CHOICES = [
        (DAILY, '1 day - 1 month'),
        (MONTHLY, '1 month - 1 year'),
        (YEARLY, '1 year or more'),
        ]

    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    info = models.TextField(blank=True,)
    photo = models.ImageField(blank=True,)
    country = models.CharField(max_length=50, blank=False,)
    city = models.CharField(max_length=50, blank=False,)
    district = models.CharField(max_length=50, blank=False,)
    created_date = models.DateTimeField(default=timezone.now)
    size = models.PositiveSmallIntegerField()
    price_per_month = models.PositiveIntegerField()
    avilable_from = models.DateField(blank=True,)
    rent_type = models.CharField(
        max_length=1,
        choices=RENT_TYPE_CHOICES,
        default=MONTHLY,
    )
    type = models.CharField(
        max_length=1,
        choices=RE_TYPE_CHOICES,
        default=FLAT,
    )

    type_other = models.CharField(max_length=50, blank=True,)


class RentPost(models.Model):

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

    DAILY = 'D'
    MONTHLY = 'M'
    YEARLY = 'Y'

    RENT_TYPE_CHOICES = [
        (DAILY, '1 day - 1 month'),
        (MONTHLY, '1 month - 1 year'),
        (YEARLY, '1 year or more'),
        ]

    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    info = models.TextField(blank=True,)
    country = models.CharField(max_length=50, blank=False,)
    city = models.CharField(max_length=50, blank=False,)
    district = models.CharField(max_length=50, blank=False,)
    created_date = models.DateTimeField(default=timezone.now)
    size_min = models.PositiveSmallIntegerField()
    size_max = models.PositiveSmallIntegerField()
    room_num = models.PositiveSmallIntegerField()
    price_per_month_min = models.PositiveIntegerField()
    price_per_month_max = models.PositiveIntegerField()
    check_in = models.DateField(blank=True,)
    check_out = models.DateField(blank=True,)
    rent_type = models.CharField(
        max_length=1,
        choices=RENT_TYPE_CHOICES,
        default=MONTHLY,
    )
    type = models.CharField(
        max_length=1,
        choices=RE_TYPE_CHOICES,
        default=FLAT,
    )

    type_other = models.CharField(max_length=50, blank=True,)

class BuyPost(models.Model):

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

    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    info = models.TextField(blank=True,)
    country = models.CharField(max_length=50, blank=False,)
    city = models.CharField(max_length=50, blank=False,)
    district = models.CharField(max_length=50, blank=False,)
    created_date = models.DateTimeField(default=timezone.now)
    size_min = models.PositiveSmallIntegerField()
    size_max = models.PositiveSmallIntegerField()
    room_num = models.PositiveSmallIntegerField()
    price_min = models.PositiveIntegerField()
    price_max = models.PositiveIntegerField()
    type = models.CharField(
        max_length=1,
        choices=RE_TYPE_CHOICES,
        default=FLAT,
    )

    type_other = models.CharField(max_length=50, blank=True,)
