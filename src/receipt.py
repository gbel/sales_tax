'''
Main file for the reicept details printer
'''

import abc
from decimal import Decimal

BASE_SALES_TAX = .10
IMPORTED_TAX = .05
TAX_EXEMPT = ('book', 'chocolate', 'chocolates', 'pills')


class BaseReceipt(object):
    """
    Meta class for all receipts 

    Attributes:
        qty: An integer representing the quantity.
        name: The integral number of miles driven on the vehicle.
        make: The make of the vehicle as a string.
    """
    __metaclass__ = abc.ABCMeta

    def __init__(self, qty, name, price):
        self.qty = qty
        self.name = name
        self.price = price

    @abc.abstractmethod
    def product_type(self):
        """Return a string representing the type of product this is."""

    @abc.abstractmethod
    def product_tax(self):
        """Return product total tax. Taking in consideration """

    @abc.abstractmethod
    def product_price(self):
        """Return product total tax."""
