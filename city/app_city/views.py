from rest_framework import generics, status
from rest_framework.response import Response
from django.utils import timezone
from .models import City, Street, Shop
from .serializers import CitySerializer, StreetSerializer, ShopSerializer


class CityList(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class StreetList(generics.ListAPIView):
    serializer_class = StreetSerializer

    def get_queryset(self):
        city_id = self.kwargs["city_id"]
        return Street.objects.filter(city_id=city_id)


class ShopCreate(generics.CreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            shop = serializer.save()
            return Response({"id": shop.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ShopList(generics.ListAPIView):
    serializer_class = ShopSerializer

    def get_queryset(self):
        queryset = Shop.objects.select_related("city", "street").all()
        city = self.request.query_params.get("city")
        street = self.request.query_params.get("street")
        open_status = self.request.query_params.get("open")

        if city:
            queryset = queryset.filter(city__name=city)
        if street:
            queryset = queryset.filter(street__name=street)

        if open_status is not None:
            current_time = timezone.now().time()
            if open_status == "1":
                queryset = queryset.filter(
                    opening_time__lte=current_time, closing_time__gte=current_time
                )
            elif open_status == "0":
                queryset = queryset.exclude(
                    opening_time__lte=current_time, closing_time__gte=current_time
                )

        return queryset
