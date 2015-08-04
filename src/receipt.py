'''
Main file for the reicept details printer
'''

import abc
import math
import re

from decimal import Decimal, getcontext, ROUND_HALF_EVEN

BASE_SALES_TAX = 0.10
IMPORTED_TAX = 0.05
TAX_EXEMPT = ('book', 'chocolate', 'chocolates', 'pills')
DICT_DB = dict()


def round_nearest(x, a=0.05):
    """
    Helper function to provide the required ROUND policy
    """
    return round(round(x / a) * a, -int(math.floor(math.log10(a))))


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

        instance.cart = DICT_DB
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
    def cart_total(self):
        """Return Receipt total with tax and all."""

    @abc.abstractmethod
    def populate_db(self):
        """Populate in memory dict()"""

    @abc.abstractmethod
    def print_receipt(self):
        """Print out receipt"""


class Receipt(BaseReceipt):
    """
    Receipt Class inherit from Base Receipt

    Attributes:
        qty: An integer representing the quantity.
        name: The integral number of miles driven on the vehicle.
        make: The make of the vehicle as a string.
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
        total = round_nearest(total.__float__())
        return float(self.price) + total

    def product_price(self):
        #tax exempt not import tax
        if self.product_tax_exempt() and not self.product_imported():
            return self.price

        #tax exempt and import tax
        if self.product_tax_exempt() and self.product_imported():
            price = self.product_tax_calculator(self.import_tax)
            return '%.2f' % price

        #base tax not import tax
        if not self.product_tax_exempt() and not self.product_imported():
            price = self.product_tax_calculator(self.base_tax)
            return '%.2f' % price

        #base tax and import tax
        if not self.product_tax_exempt() and self.product_imported():
            price = self.product_tax_calculator(self.base_tax + self.import_tax)
            return '%.2f' % price

    def cart_total(self):
        pass

    def populate_db(self):
        pass

    def print_receipt(self):
        pass
