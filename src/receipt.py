'''
Main file for the reicept details printer
'''

import abc
import math
import re
import shelve

from decimal import Decimal, getcontext, ROUND_HALF_EVEN

BASE_SALES_TAX = 0.10
IMPORTED_TAX = 0.05
TAX_EXEMPT = ('book', 'chocolate', 'chocolates', 'pills')
RECEIPT_DB = shelve.open('receipts.db')

def round_nearest(price, a=0.05):
    """
    Helper function to provide the required ROUND policy
    """
    return round(round(price / a) * a, -int(math.floor(math.log10(a))))


class BaseReceipt(object):
    """
    Meta class for all receipts

    """
    __metaclass__ = abc.ABCMeta

    __slots__ = ["cart", "base_tax", 'import_tax']
    """
    Slots define [template] abstract class attributes. No instance
    __dict__ will be present unless subclasses create it through
    implicit attribute definition in __init__()
    """
    def __new__(cls, *args, **kwargs):
        """
        Factory method for base/subtype creation. Simply creates an
        (new-style class) object instance and sets a base properties.
        """
        instance = object.__new__(cls)

        instance.base_tax = BASE_SALES_TAX
        instance.import_tax = IMPORTED_TAX

        return instance

    @abc.abstractmethod
    def product_tax_exempt(self):
        """Return True if product is tax exempt. Based on name."""

    @abc.abstractmethod
    def product_imported(self):
        """Return True if product is imported. Based on name."""

    @abc.abstractmethod
    def product_tax_calculator(self, tax_rate):
        """Apply tax rate to product price. Returns a float"""

    @abc.abstractmethod
    def product_price(self):
        """Return product total price with tax and all."""

    @abc.abstractmethod
    def receipt_save_item(self):
        """
        Save cart to shelf. Dict structure:
            {
              items: { {
                       qty: 1,
                       name: `product_name`,
                       price: `price_with_tax`]
                       }, },
               sales_tax: 'total_tax',
               total: 'receipt_total'
            }
        """

    @abc.abstractmethod
    def receipt_retrieve(self, id):
        """Retrieve given id from shelf"""

    @abc.abstractmethod
    def print_receipt(self):
        """Print out receipt"""


class Receipt(BaseReceipt):
    """
    Receipt Class inherit from Base Receipt

    Attributes:
        qty: An integer representing the quantity.
        name: The name of product (string).
        price: The product price (string).
    """
    def __init__(self, qty, name, price):
        self.qty = qty
        self.name = name
        self.price = price

    def product_tax_exempt(self):
        tax_exempt = re.compile(r''+'|'.join(str(i) for i in TAX_EXEMPT))
        if tax_exempt.search(self.name):
            return True
        else:
            return False

    def product_imported(self):
        imported = re.compile(r'imported')
        if imported.search(self.name):
            return True
        else:
            return False

    def product_tax_calculator(self, tax_rate):
        #setup decimal context
        getcontext().prec = 4
        getcontext().round = ROUND_HALF_EVEN
        total = Decimal(self.price) * Decimal(tax_rate)
        return round_nearest(total.__float__())

    def product_price(self):
        #tax exempt not import tax
        if self.product_tax_exempt() and not self.product_imported():
            return float(self.price)

        #tax exempt and import tax
        if self.product_tax_exempt() and self.product_imported():
            return round(float(self.price) + self.product_tax_calculator(self.import_tax),2)

        #base tax not import tax
        if not self.product_tax_exempt() and not self.product_imported():
            return round(float(self.price) + self.product_tax_calculator(self.base_tax),2)

        #base tax and import tax
        if not self.product_tax_exempt() and self.product_imported():
            return round(float(self.price) + self.product_tax_calculator(self.base_tax + self.import_tax),2)

    def receipt_save_item(self, id):
        data = dict(items=[dict(
                                qty=self.qty,
                                name=self.name,
                                price=self.product_price),
                          ],
                    sales_tax=self.product_tax_calculator,
                    total=self.product_price)
        return data

    def receipt_retrieve(self, id):
        pass

    def print_receipt(self):
        pass
