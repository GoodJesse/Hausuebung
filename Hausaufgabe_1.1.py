"""
Name:Jesse Ziegler
Datum:03.10.2018

1. Hausaufgabe am 03.10.2018
"""

#Variablen definieren
a = 2
b = 3
y = 3

#berechnen
x = a*(1-(y/b)**2)**(0.5)

#ausgeben
print __doc__
print "x = %s, y = %s" %(x,y)

#für andere y-Werte
#Variablen initialisieren
y1 = 1
y2 = 1.

#berechnen
x1 = a*(1-((y1/b)**2))**(0.5)
x2 = a*(1-((y2/b)**2))**(0.5)

#neue Ergebnisse ausgeben
print "fuer y = 1: %s, fuer y = 1.: %s" %(x1,x2)

"""
Wieso unterscheiden sich die Ergebnisse?
Bei y=1 wird bloß mit ganzen Zahlen gerechnet, da alle Zahlen als ganze Zahlen definiert wurden. 
Dadurch ist das Ergebnis bloß eine Rundung
Bei y=1. ist die Variable eine float Variable, dass bedeutet das sie eine Dezimalzahl ist. 
Alle Rechnungen werden also mit Dezimalzahlen durchgeführt und ist somit das sinnvollere Ergebnis. 
Jedoch sind beide Varianten mathematisch richtig.
"""