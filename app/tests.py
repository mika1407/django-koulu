from django.http import response
from django.test import TestCase, Client
import unittest
from django.urls import reverse


from .laskin import plus, plus_complicated
from .models import Supplier, Product
from .views import supplierlistview, productlistview
client = Client()

class ListMethodTests(TestCase):
  def test_listing_products(self):
    ''' palauttaa statuskoodin 200 '''
    response = client.get(reverse(productlistview))
    self.assertEqual(response.status_code, 200)

  def test_listing_suppliers(self):
    ''' palauttaa statuskoodin 200 '''
    response = client.get(reverse(supplierlistview))
    self.assertEqual(response.status_code, 200)

class SupplierModelTests(TestCase):
  def setUp(self):
    Supplier.objects.create(companyname="Test company", contactname="Jaakko Kulta", address="Kultatie 1", phone="1234567", email="jaakko@gmail.com", country="Finland")

  def test_added_supplier_exists(self):
        """ added supplier exists and can be searched"""
        supplier = Supplier.objects.get(companyname="Test company")
        self.assertEqual(supplier.address, "Kultatie 1")
        self.assertEqual(supplier.country, "Finland")


class LaskinTests(TestCase):
    def test_plus(self):
        # testaa että numerot lasketaan yhteen oikein
        self.assertEqual(plus(7, 2), 9)
        self.assertEqual(plus(7.20, 2.70), 9.90)
        self.assertEqual(plus(-7, 2), -5)

    def test_plus_complicated(self):
        # testaa ehdollisen yhteenlaskun toimivuus
        self.assertEqual(plus_complicated(7, 2), 9)
        self.assertEqual(plus_complicated(2, 8), 8)

    @unittest.expectedFailure
    def test_plus_should_fail(self):
        self.assertEqual(plus(7, '2'), '9')
        self.assertEqual(plus(7, '2'), 9)
        self.assertEqual(plus('7', '2'), '9')
        self.assertEqual(plus(7.1, 2.1), 9.2)

    # TDD - Test Driven Development
    '''testi, toiminto, refaktotointi, testi, ... uudistus, testi'''
