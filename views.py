from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import *

@api_view(['GET'])
def get_country(request):
    country = Country.objects.all()
    serialized_data = CountrySerializer(country, many=True)
    return Response(serialized_data.data)

@api_view(['GET'])
def get_region(request, pk):
    region = Region.objects.filter(country_id=pk)
    serialized_data = RegionSerializer(region, many=True)
    return Response(serialized_data.data)

@api_view(['GET'])
def get_category(request, pk, region):
    if region == 1:
      region = Region.objects.get(id=pk)
      category = region.category.all()
      serialized_data = CategorySerializer(category, many=True)
    else:
        town = Town.objects.get(id=pk)
        category = region.category.all()
        serialized_data = CategorySerializer(category, many=True)
    return Response(serialized_data.data)

@api_view(['GET'])
def get_town(request, pk):
    towns = Town.object.filter(region_id=pk)
    serialized_data = TownSerializer(towns, many=True)
    return Response(serialized_data.data)

@api_view(['GET'])
def get_place(request, pk):
    region_id = request.GET.get('region')
    region_or_town = int(request.GET.get('region_or_town'))
    if region_or_town == 1:
        place = Place.objects.filter(category_id=pk, region_id=region_id)
    elif region_or_town == 0:
        place = Place.objects.filter(category_id=pk,town_id=region_id)
    serialized_data = PlaceSerializer(place, many=True)
    return Response(serialized_data.data)