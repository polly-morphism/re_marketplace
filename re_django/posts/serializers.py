from rest_framework import serializers
from posts.models import SellPost, RentOutPost


class SellPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellPost
        fields = [
        'seller', 'info', 'photo', 'country', 'city',
        'district', 'created_date', 'published_date', 'size', 'price', 'type', 'type_other',
        ]

    def create(self, validated_data):
        return SellPost.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.seller = validated_data.get('seller', instance.seller)
        instance.info = validated_data.get('info', instance.info)
        instance.photo = validated_data.get('photo', instance.photo)
        instance.country = validated_data.get('country', instance.country)
        instance.city = validated_data.get('city', instance.city)
        instance.district = validated_data.get('district', instance.district)
        instance.created_date = validated_data.get('created_date', instance.created_date)
        instance.published_date = validated_data.get('published_date', instance.published_date)
        instance.size = validated_data.get('size', instance.size)
        instance.price = validated_data.get('price', instance.price)
        instance.type = validated_data.get('type', instance.type)
        instance.type_other = validated_data.get('type_other', instance.type_other)

        instance.save()
        return instance

class RentOutPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentOutPost
        fields = [
        'seller', 'info', 'photo', 'country', 'city',
        'district', 'created_date', 'size', 'price_per_month', 'avilable_from', 'rent_type',
        'type', 'type_other',
        ]

    def create(self, validated_data):
        return RentOutPost.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.seller = validated_data.get('seller', instance.seller)
        instance.info = validated_data.get('info', instance.info)
        instance.photo = validated_data.get('photo', instance.photo)
        instance.country = validated_data.get('country', instance.country)
        instance.city = validated_data.get('city', instance.city)
        instance.district = validated_data.get('district', instance.district)
        instance.created_date = validated_data.get('created_date', instance.created_date)
        instance.size = validated_data.get('size', instance.size)
        instance.price_per_month = validated_data.get('price_per_month', instance.price_per_month)
        instance.avilable_from = validated_data.get('avilable_from', instance.avilable_from)
        instance.rent_type = validated_data.get('rent_type', instance.rent_type)
        instance.type = validated_data.get('type', instance.type)
        instance.type_other = validated_data.get('type_other', instance.type_other)



        instance.save()
        return instance
