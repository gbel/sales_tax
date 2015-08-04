import unittest

from receipt import Receipt

class TestReceipt(unittest.TestCase):

    def setUp(self):
        self.input1_a = Receipt(1, 'book', '12.49')
        self.input1_b = Receipt(1, 'music CD', '14.99')
        self.input1_c = Receipt(1, 'chocolate bar', '0.85')

        self.input2_a = Receipt(1, 'imported box of chocolates', '10.00')
        self.input2_b = Receipt(1, 'imported bottle of perfume', '47.50')

        self.input3_a = Receipt(1, 'imported bottle of perfume', '27.99')
        self.input3_b = Receipt(1, 'bottle of perfume', '18.99')
        self.input3_c = Receipt(1, 'packet of headache pills', '9.75')
        self.input3_d = Receipt(1, 'box of imported chocolates', '11.25')

    def test_tax_exempt_products(self):
        self.assertTrue(self.input1_a.product_tax_exempt())
        self.assertFalse(self.input1_b.product_tax_exempt())
        self.assertTrue(self.input1_c.product_tax_exempt())
        self.assertTrue(self.input2_a.product_tax_exempt())

    def test_imported_products(self):
        self.assertTrue(self.input2_a.product_imported())
        self.assertFalse(self.input3_b.product_imported())

    def test_product_price(self):
        self.assertEqual(self.input1_a.product_price(), '12.49')
        self.assertEqual(self.input1_b.product_price(), '16.49')
        self.assertEqual(self.input2_a.product_price(), '10.50')
        self.assertEqual(self.input2_b.product_price(), '54.65')
        self.assertEqual(self.input3_a.product_price(), '32.19')
