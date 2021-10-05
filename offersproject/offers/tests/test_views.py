from rest_framework import status
from rest_framework.test import APITestCase

from offers.tests import factories
from offers import models

class CategoryViewSetTestCase(APITestCase):

    def setUp(self):
        self.category1 = factories.CategoryFactory()

    def test_category_get_list(self):
        response = self.client.get('/category/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_category_get_details_not_allowed(self):
        response = self.client.get('/category/{}/'.format(self.category1.id))
        self.assertEqual(response.status_code,
            status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_category_post(self):
        data = {'name': 'category3', 'ordering': 1}
        response = self.client.post('/category/', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(models.Category.objects.filter(name='category3').exists())

    def test_category_delete(self):
        response = self.client.delete('/category/{}/'.format(self.category1.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(
            models.Category.objects.filter(name='category1').exists())

    def test_category_put(self):
        data = {'name': 'category3'}
        response = self.client.put('/category/{}/'.format(self.category1.id),
            data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(
            models.Category.objects.filter(name='category3').exists())

class OfferViewSetTestCase(APITestCase):

    def setUp(self):
        self.category1 = factories.CategoryFactory()
        self.category2 = factories.CategoryFactory(name='cat_2', ordering=2)
        self.offer1 = factories.OfferFactory()

    def test_offer_list_get(self):
        response = self.client.get('/offers/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_offer_get_details(self):
        response = self.client.get('/offers/{}/'.format(self.offer1.id))
        self.assertEqual(response.status_code,
            status.HTTP_200_OK)

    def test_offer_post(self):
        data = {
            'title': 'test_title',
            'description': 'desc',
            'price': 30,
            'category': self.category1.id}
        response = self.client.post('/offers/', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(models.Offer.objects.filter(
            title=data['title']).exists())

    def test_offer_put(self):
        data = {
            'title': 'test_title',
            'description': 'desc',
            'price': 30,
            'category': self.category1.id}
        response = self.client.put('/offers/{}/'.format(self.offer1.id),
            data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(models.Offer.objects.filter(
            title=data['title']).exists())

    def test_offer_delete(self):
        response = self.client.delete('/offers/{}/'.format(self.offer1.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(
            models.Offer.objects.filter(title='offer1').exists())
