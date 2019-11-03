from django.test import TestCase
from .models import Product

# Create your tests here.
# Test is from the code institute #
class ProductTests(TestCase):
    """
    Here we'll define the tests that we'll run against our
    Product model
    """

    def test_str(self):
        test_title = Product(title='A product')
        self.assertEqual(str(test_title), 'A product')