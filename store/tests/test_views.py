from django.contrib.auth.models import User
from django.http import HttpRequest
from django.test import Client, RequestFactory, TestCase
from django.urls import reverse

from store.models import Category, Product, Supplier
from store.views import products_all
from importlib import import_module
from django.conf import settings


class TestViewResponses(TestCase):
    def setUp(self):
        self.c = Client()
        self.factory = RequestFactory()
        User.objects.create(username='admin')
        Category.objects.create(name='eat', slug='eat')
        Supplier.objects.create(name='louis', email='louisdejager@gmail.com')
        Product.objects.create(category_id=1, name='single origin coffee', created_by_id=1,
                               slug='single-origin-coffee', price='20', image='django', supplier_id=1)

    def test_url_allowed_hosts(self):
        """
        Test Allowed hosts
        """
        response = self.c.get('/', HTTP_HOST='noaddress.com')
        self.assertEqual(response.status_code, 400)
        response = self.c.get('/', HTTP_HOST='baardandco.com')
        self.assertEqual(response.status_code, 200)

    def test_product_detail_url(self):
        """
        Test reverse function for products in the models
        """
        response = self.c.get(reverse('store:product_detail', args=['single-origin-coffee']))
        self.assertEqual(response.status_code, 200)

    def test_category_list_url(self):
        """
        Test reverse function for categories in the models
        """
        response = self.c.get(reverse('store:category_list', args=['eat']))
        self.assertEqual(response.status_code, 200)

    def test_homepage_html(self):
        request = HttpRequest()
        engine = import_module(settings.SESSION_ENGINE)
        request.session = engine.SessionStore()
        response = products_all(request)
        html = response.content.decode('utf-8')
        self.assertIn('<title>BAARD &amp; CO</title>', html)
        self.assertTrue(html.startswith('<!doctype html>\n<html lang="en">\n'))
        self.assertEqual(response.status_code, 200)
