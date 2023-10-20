from rest_framework import serializer
from .models import *

class CountrySerializer(serializer.ModelSerializer):
    class Meta:
        modal = Country
        fields = "__all__"


class RegionSerializer(serializer.ModelSerializer):
    category = CategorySerializer(read_only=True, many=True)
    class Meta:
        modal = Region
        fields = "__all__"


class CategorySerializer(serializer.ModelSerializer):
    class Meta:
        modal = Category
        fields = "__all__"


class TownSerializer(serializer.ModelSerializer):
    class Meta:
        modal = Town
        fields = "__all__"


class  PlaceSerializer(serializer.ModelSerializer):
    class Meta:
        depth = 1
        modal = Place
        fields = "__all__"

