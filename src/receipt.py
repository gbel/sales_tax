'''
Main file for the reicept details printer
'''

import abc
import re

from decimal import Decimal

BASE_SALES_TAX = .10
IMPORTED_TAX = .05
TAX_EXEMPT = ('book', 'chocolate', 'chocolates', 'pills')
DICT_DB = dict()


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

    def product_price(self):
        if self.product_tax_exempt() and not self.product_imported():
            return self.price

    def cart_total(self):
        pass

    def populate_db(self):
        pass

    def print_receipt(self):
        pass
