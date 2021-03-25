from django.contrib.auth.models import User
from django.test import TestCase

from store.models import Category, Product, Supplier


class TestCategoriesModel(TestCase):
    def setUp(self):
        self.data1 = Category.objects.create(name='django', slug='django')

    def test_category_model_entry(self):
        """
        Test Category model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))

    def test_category_model_default_name(self):
        """
        Test Category model default name
        """
        data = self.data1
        self.assertEqual(str(data), 'django')


class TestProductModel(TestCase):
    def setUp(self):
        Category.objects.create(name='django', slug='django')
        Supplier.objects.create(name='louis', email='louisdejager@gmail.com')
        User.objects.create(username='admin')
        self.data1 = Product.objects.create(category_id=1, name='single origin coffee', created_by_id=1,
                                            slug='single-origin-coffee', price='20', image='django', supplier_id=1)

    def test_products_model_entry(self):
        """
        Test Category model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Product))

    def test_products_model_default_name(self):
        """
        Test Category model default name
        """
        data = self.data1
        self.assertEqual(str(data), 'single origin coffee')


class TestSupplierModel(TestCase):
    def setUp(self):
        self.data1 = Supplier.objects.create(name='Coffee Roasters', email='coffeeroasters@gmail.com')

    def test_supplier_model_entry(self):
        """
        Test Category model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Supplier))

    def test_supplier_model_default_name(self):
        """
        Test Category model default name
        """
        data = self.data1
        self.assertEqual(str(data), 'Coffee Roasters')
