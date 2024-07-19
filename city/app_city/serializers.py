from rest_framework import serializers
from .models import City, Street, Shop


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"


class StreetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Street
        fields = "__all__"


class ShopSerializer(serializers.ModelSerializer):
    city_name = serializers.CharField(source="city.name", read_only=True)
    street_name = serializers.CharField(source="street.name", read_only=True)

    class Meta:
        model = Shop
        fields = [
            "id",
            "name",
            "city",
            "city_name",
            "street",
            "street_name",
            "building",
            "opening_time",
            "closing_time",
        ]
