#!/usr/bin/env python

from receipt import Receipt

if __name__ == '__main__':
    input1_a = Receipt(1, 'book', '12.49')
    input1_a.receipt_save_item('input1')
    input1_b = Receipt(1, 'music CD', '14.99')
    input1_b.receipt_save_item('input1')
    input1_c = Receipt(1, 'chocolate bar', '0.85')
    input1_c.receipt_save_item('input1')

    receipt_1 = input1_c

    input2_a = Receipt(1, 'imported box of chocolates', '10.00')
    input2_b = Receipt(1, 'imported bottle of perfume', '47.50')

    input3_a = Receipt(1, 'imported bottle of perfume', '27.99')
    input3_b = Receipt(1, 'bottle of perfume', '18.99')
    input3_c = Receipt(1, 'packet of headache pills', '9.75')
    input3_d = Receipt(1, 'box of imported chocolates', '11.25')
