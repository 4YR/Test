from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import City, Street, Shop


class CityTests(APITestCase):
    
    def setUp(self):
        self.city = City.objects.create(name='Samara')
        
    def test_get_cities(self):
        url = reverse('city-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_create_city(self):
        url = reverse('city-list')
        data = {'name': 'New-York'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(City.objects.count(), 2)
        

class ShopTests(APITestCase):
    
    def setUp(self):
        self.city = City.objects.create(name="Voronez")
        self.street = Street.objects.create(name="Тверская", city=self.city)

    def test_create_shop(self):
        url = reverse('shop-create')
        data = {
            'name': 'Магазин 3',
            'city': self.city.id,
            'street': self.street.id,
            'building': '1',
            'opening_time': '09:00',
            'closing_time': '21:00'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Shop.objects.count(), 1)
