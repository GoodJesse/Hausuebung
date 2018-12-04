# -*- coding: utf-8 -*-
"""
Name:Jesse Ziegler
Datum:22.10.2018

2. Hausaufgabe am 31.10.2018
"""

#definiere Variablen
Halbachsen = ["a = 4.12", "b = 13.2", "c=4.25"]
Ellipsoid = {}


a = Halbachsen[0].split("=")[1].strip(" ")
b = Halbachsen[1].split("=")[1].strip(" ")
c = Halbachsen[2].split("=")[1].strip(" ")

Volumen = 3.1415*4/3.*a*b*c

Ellipsoid['a'] = 2*a
Ellipsoid['b'] = 2*b
Ellipsoid['c'] = 2*c

#ausgeben des Volumens mit drei Nachkommastellen
print "Volumen: %.3f" %(Volumen)

#Ellipsoid Dictionary ausgeben
print "\nEllipsoid-Dictionary: %s" %Ellipsoid

Volumen = 3.1415*4/3.
abc = ['a','b','c']

#Liste mit Zahlenwerten finden
for Halbachse in Halbachsen:
    #Halbachse zu Volumen multiplizieren
    Volumen *= float(Halbachse.split("=")[1].strip(" "))
    
    #ins Dictionary eintragen (Mal zwei da ganze Achse)
    Ellipsoid[abc[Halbachsen.index(Halbachse)]] = 2*float(Halbachse.split("=")[1].strip(" "))
    
#ausgeben des Volumens mit drei Nachkommastellen
print "Volumen: %.3f" %(Volumen)

#Ellipsoid Dictionary ausgeben
print "\nEllipsoid-Dictionary: %s" %Ellipsoid

"""
Getestet mit folgenden Liste:
["a = 4.12", "b =  13", "c=4.25"]
["a =  4", "b = 3", "c= 5"]
["a=6.7", "b =  5.9", "c=0.75"]
["a = 5.45", "b= 1", "c=9.5"]
"""
