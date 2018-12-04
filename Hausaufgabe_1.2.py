"""
Name:Jesse Ziegler
Datum:03.10.2018

1. Hausaufgabe am 03.10.2018
"""

print __doc__

#Variable Bytes definieren
Bytes = 4
print "Bytes:", Bytes

#Anzahl der Möglichen Stellungen Berechnen
Bits = Bytes*8
groesteZahl = 2**Bits-1

#ausgeben
print "\n%s" %(groesteZahl)
