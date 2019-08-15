from rest_framework import serializers
from api.models import Seller, SellerInfo
from comments.models import Rating
from comments.serializers import RatingSerializer
from django.db.models import Avg


class SellerInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = SellerInfo
        fields = (
        'user',
        'seller_name',
        'info',
        'photo',
        'dob',
        'country',
        'city',
        'phone',
        'seller_type',
        'company_name',
        'compane_site',
        )


class SellerSerializer(serializers.HyperlinkedModelSerializer):
    profile = SellerInfoSerializer(required=True)
    ####
    comments = RatingSerializer(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField()
    #####
    class Meta:
        model = Seller
        fields = ('url', 'email', 'first_name', 'last_name', 'password', 'profile', 'comments', 'average_rating') # <--- 2 new
        extra_kwargs = {
        'password': {'write_only': True},
        }


    def create(self, validated_data):
        password = validated_data.pop('password')
        user = Seller(**validated_data)
        user.set_password(password)
        user.save()
        SellerInfo.objects.create(user=user, **profile_data)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile

        instance.email = validated_data.get('email', instance.email)
        instance.save()

        profile.user = profile_data.get('user', profile.user)
        profile.seller_name = profile_data.get('seller_name', profile.seller_name)
        profile.info = profile_data.get('info', profile.info)
        profile.dob = profile_data.get('dob', profile.dob)
        profile.city = profile_data.get('city', profile.city)
        profile.country = profile_data.get('country', profile.country)
        profile.phone = profile_data.get('phone', profile.phone)
        profile.seller_type = profile_data.get('seller_type', profile.seller_type)
        profile.company_name = profile_data.get('company_name', profile.company_name)
        profile.compane_site = profile_data.get('compane_site', profile.compane_site)
        profile.photo = profile_data.get('photo', profile.photo)
        profile.save()

        return instance

    def get_average_rating(self, obj):
        average = obj.comments.aggregate(Avg('rating')).get('rating__avg')
        if average is None:
            return 0
        else:
            return round(average*2) / 2


"""
 reviews = serializers.PrimaryKeyRelatedField(
            many=True,
            read_only=True
        )
        average_rating = serializers.SerializerMethodField()

        class Meta:
            model = models.Course
            fields = (
                'id',
                'title',
                'url',
                'reviews',
                'average_rating'
            )

        def get_average_rating(self, obj):
            average = obj.reviews.aggregate(Avg('rating')).get('rating__avg')
            if average is None:
                return 0
            else:
                return round(average*2) / 2

"""
