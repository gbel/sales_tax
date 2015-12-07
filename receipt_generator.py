#!/usr/bin/env python

from receipt.receipt import Receipt

def receipt_printout(receipt, header=None):
    """ Print out passed receipt """
    print
    if header:
        print(header)
    for item in receipt['items']:
        print("{0} {1}: {2}".format(item['qty'], item['name'], item['price']))

    print("Sales Taxes: {0}".format(receipt['sales_tax']))
    print("Total: {0}".format(receipt['total']))


if __name__ == '__main__':
    input1_a = Receipt(1, 'book', '12.49')
    input1_a.receipt_save_item('input1')
    input1_b = Receipt(1, 'music CD', '14.99')
    input1_b.receipt_save_item('input1')
    input1_c = Receipt(1, 'chocolate bar', '0.85')
    input1_c.receipt_save_item('input1')

    receipt_1 = input1_c.receipt_checkout('input1')
    receipt_printout(receipt_1, 'Output 1')

    input2_a = Receipt(1, 'imported box of chocolates', '10.00')
    input2_a.receipt_save_item('input2')
    input2_b = Receipt(1, 'imported bottle of perfume', '47.50')
    input2_b.receipt_save_item('input2')

    receipt_2 = input2_b.receipt_checkout('input2')
    receipt_printout(receipt_2, 'Output 2')

    input3_a = Receipt(1, 'imported bottle of perfume', '27.99')
    input3_a.receipt_save_item('input3')
    input3_b = Receipt(1, 'bottle of perfume', '18.99')
    input3_b.receipt_save_item('input3')
    input3_c = Receipt(1, 'packet of headache pills', '9.75')
    input3_c.receipt_save_item('input3')
    input3_d = Receipt(1, 'box of imported chocolates', '11.25')
    input3_d.receipt_save_item('input3')

    receipt_3 = input3_d.receipt_checkout('input3')
    receipt_printout(receipt_3, 'Output 3')
