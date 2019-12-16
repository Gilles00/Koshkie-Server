from rest_framework import serializers

from shops.models import (ShopProfileModel, ProductGroupModel, ProductModel,
                          OptionGroupModel, OptionModel, AddOn, RelyOn,
                          ShopAddressModel, ShopReviewModel, ProductReviewModel)
from users.serializers import UserProfileSerializer


class RelyOnSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelyOn
        fields = ('choosed_option_group', 'option')


class AddOnSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddOn
        fields = ('title', 'sort', 'added_price')
        extra_kwargs = {
            'sort': {'read_only': True}
        }


class OptionSerializer(serializers.ModelSerializer):
    rely_on = RelyOnSerializer(required=False)

    class Meta:
        model = OptionModel
        fields = ('title', 'sort', 'price', 'rely_on')
        extra_kwargs = {
            'sort': {'read_only': True}
        }


class OptionGroupSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True)

    class Meta:
        model = OptionGroupModel
        fields = ('options', 'title', 'sort', 'changes_price')
        extra_kwargs = {
            'sort': {'read_only': True}
        }


class ProductReviewSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer(many=False, read_only=True)

    class Meta:
        model = ProductReviewModel
        fields = ('user', 'stars', 'title', 'text', 'time_stamp')
        extra_kwargs = {
            'time_stamp': {'read_only': True},
            'user': {'read_only': True}
        }


class ProductDetailsSerializer(serializers.ModelSerializer):
    reviews = ProductReviewSerializer(many=True, read_only=True)
    option_groups = OptionGroupSerializer(many=True, required=False)
    add_ons = AddOnSerializer(many=True, required=False)

    class Meta:
        model = ProductModel
        fields = ('id', 'photo', 'title', 'description', 'base_price', 'is_available',
                  'option_groups', 'add_ons', 'reviews')
        extra_kwargs = {
            'id': {'read_only': True},
            'is_available': {'write_only': True},
            'reviews': {'read_only': True}
        }


class ProductSerializer(serializers.ModelSerializer):
    option_groups = OptionGroupSerializer(many=True, required=False)
    add_ons = AddOnSerializer(many=True, required=False)

    class Meta:
        model = ProductModel
        fields = ('id', 'photo', 'title', 'base_price', 'option_groups', 'add_ons')
        extra_kwargs = {
            'id': {'read_only': True}
        }


class ProductGroupSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = ProductGroupModel
        fields = ('title', 'sort', 'products')


class ShopAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopAddressModel
        exclude = 'shop'
        extra_kwargs = {
            'special_notes': {'required': False}
        }


class ShopReviewSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer(read_only=True)

    class Meta:
        model = ShopReviewModel
        fields = ('user', 'stars', 'title', 'text', 'time_stamp')
        extra_kwargs = {
            'time_stamp': {'read_only': True},
            'user': {'read_only': True}
        }


class ShopProfileDetailSerializer(serializers.ModelSerializer):
    address = ShopAddressSerializer()
    in_favourites_list = serializers.BooleanField(read_only=True)

    class Meta:
        model = ShopProfileModel
        fields = ('id', 'profile_photo', 'phone_number', 'shop_type', 'name',
                  'address', 'rating', 'is_open', 'currency',
                  'minimum_charge', 'delivery_fee', 'vat')
        extra_kwargs = {
            'id': {'read_only': True},
            'rating': {'read_only': True},
            'is_open': {'write_only': True}
        }


class ShopProfileSerializer(serializers.ModelSerializer):
    address = ShopAddressSerializer()

    class Meta:
        model = ShopProfileModel
        fields = ('profile_photo', 'shop_type', 'name', 'address', 'rating')