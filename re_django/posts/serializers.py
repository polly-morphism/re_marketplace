from rest_framework import serializers
from posts.models import SellPost


class SellPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellPost
        fields = [
        'seller', 'info', 'photo', 'country', 'city',
        'district', 'created_date', 'published_date', 'size', 'type', 'type_other'
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
        instance.type = validated_data.get('type', instance.type)
        instance.type_other = validated_data.get('type_other', instance.type_other)

        instance.save()
        return instance
