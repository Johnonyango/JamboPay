from django.test import TestCase
from .models import *

class IndustryTestClass(TestCase):
    def setUp(self):
        self.hospitality = Industry(name = 'Hospitality')

    def test_instance(self):
        self.assertTrue(isinstance(self.hospitality,Industry))
