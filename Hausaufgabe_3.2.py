# -*- coding: utf-8 -*-
"""
Name:Jesse Ziegler
Datum:02.11.2018

3. Hausaufgabe am 07.11.2018
"""

Zahl = 'abf573'
Zeichen = '0123456789abcdefABCDEF'

def hexadezimal(Zahl):
    for Buchstabe in str(Zahl):
        if Buchstabe not in Zeichen:
            return False
    return int(str(Zahl), 16)

print hexadezimal(Zahl)
print hexadezimal('f5')
print hexadezimal('z54fab')
print hexadezimal(3)
print hexadezimal('76')