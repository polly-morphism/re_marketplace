from rest_framework import serializers
from comments.models import Rating


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = [
        'from_user', 'user_to', 'text', 'rating', 'created_date'
        ]

    def create(self, validated_data):
        return Rating.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.from_user = validated_data.get('from_user', instance.from_user)
        instance.user_to = validated_data.get('user_to', instance.user_to)
        instance.text = validated_data.get('text', instance.text)
        instance.rating = validated_data.get('rating', instance.rating)
        instance.created_date = validated_data.get('created_date', instance.created_date)

        instance.save()
        return instance
