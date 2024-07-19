from django.urls import path

from .views import CityList, ShopCreate, ShopList, StreetList

urlpatterns = [
    path('city/', CityList.as_view(), name='city-list'),
    path('city/<int:city_id>/street/', StreetList.as_view(), name='street-list'),
    path('shop/', ShopCreate.as_view(), name='shop-create'),
    path('shop/list/', ShopList.as_view(), name='shop-list'),
]
