from django.contrib import admin
from .models import SellPost, RentOutPost, RentPost, BuyPost

admin.site.register(SellPost)
admin.site.register(RentOutPost)
admin.site.register(RentPost)
admin.site.register(BuyPost)
