from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from store.models import Category, Product, Supplier


class TestViewResponses(TestCase):
    def setUp(self):
        User.objects.create(username='admin')
        Category.objects.create(name='eat', slug='eat')
        Supplier.objects.create(name='louis', email='louisdejager@gmail.com')
        Product.objects.create(category_id=1, name='single origin coffee', created_by_id=1,
                               slug='single-origin-coffee', price='120', image='django', supplier_id=1)
        Product.objects.create(category_id=2, name='miss poppy', created_by_id=1,
                               slug='miss-poppy', price='64', image='django', supplier_id=1)
        Product.objects.create(category_id=3, name='Thandi', created_by_id=1,
                               slug='Thandi', price='64', image='django', supplier_id=1)
        self.client.post(
            reverse('basket:basket_add'), {"productid": 1, "productqty": 1, "action": "post"}, xhr=True)
        self.client.post(
            reverse('basket:basket_add'), {"productid": 2, "productqty": 2, "action": "post"}, xhr=True)

    def test_basket_url(self):
        """
        Test homepage response status
        """
        response = self.client.get(reverse('basket:basket_summary'))
        self.assertEqual(response.status_code, 200)

    def test_basket_add(self):
        """
        Test adding items to the basket
        """
        response = self.client.post(
            reverse('basket:basket_add'), {"productid": 3, "productqty": 1, "action": "post"}, xhr=True)
        self.assertEqual(response.json(), {'qty': 4})
        response = self.client.post(
            reverse('basket:basket_add'), {"productid": 2, "productqty": 1, "action": "post"}, xhr=True)
        self.assertEqual(response.json(), {'qty': 3})

    def test_basket_delete(self):
        """
        Test deleting items from the basket
        """
        response = self.client.post(
            reverse('basket:basket_delete'), {"productid": 2, "action": "post"}, xhr=True)
        self.assertEqual(response.json(), {'qty': 1, 'subtotal': '20.00'})

    def test_basket_update(self):
        """
        Test updating items from the basket
        """
        response = self.client.post(
            reverse('basket:basket_update'), {"productid": 2, "productqty": 1, "action": "post"}, xhr=True)
        self.assertEqual(response.json(), {'qty': 2, 'subtotal': '40.00'})