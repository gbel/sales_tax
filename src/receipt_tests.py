import unittest

from receipt import Receipt

class TestReceipt(unittest.TestCase):
    def test_tax_exempt_products(self):
        self.assertTrue(Receipt(1, 'book', 10).product_tax_exempt())
        self.assertFalse(Receipt(1, 'Music CD', 10).product_tax_exempt())
        self.assertTrue(Receipt(1, 'chocolate bar', 10).product_tax_exempt())
        self.assertTrue(Receipt(1, 'imported box of chocolates', 10).product_tax_exempt())

    def test_imported_products(self):
        self.assertTrue(Receipt(1, 'imported box of chocolates', 10).product_imported())
        self.assertFalse(Receipt(1, 'Music CD', 10).product_imported())
