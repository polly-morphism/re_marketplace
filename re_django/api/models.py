from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from phonenumber_field.modelfields import PhoneNumberField


class Seller(AbstractUser):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=64, blank=True, null=True)
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return "{}".format(self.email)

class SellerInfo(models.Model):
    PRIVATE = 'PR'
    COMPANY = 'CO'

    SELLER_TYPE_CHOICES = [
        (PRIVATE, 'Private'),
        (COMPANY, 'Company'),
    ]

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    seller_name = models.CharField(max_length=64)
    info = models.TextField(blank=True,)
    photo = models.ImageField(blank=True,)
    dob = models.DateField(blank=True,)
    country = models.CharField(max_length=50, blank=True,)
    city = models.CharField(max_length=50, blank=True,)
    phone = PhoneNumberField(null=False, blank=True, unique=True,)
    seller_type = models.CharField(
        max_length=2,
        choices=SELLER_TYPE_CHOICES,
        default=PRIVATE,
    )
    company_name = models.CharField(max_length=64, blank=True,)
    compane_site = models.URLField(max_length=128, blank=True,)
