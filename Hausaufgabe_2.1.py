# -*- coding: utf-8 -*-
"""
Name:Jesse Ziegler
Datum:22.10.2018

2. Hausaufgabe am 31.10.2018
"""

#Variablen definieren
Preise = [1.50, 0.99, 12.40, 0.99, 15.25]
i = 1
x = 0
NeuePreise = []

#herausfinden, ob 0.99 in der Liste ist
if Preise.count(0.99) > 0:
    print "0.99c ist in der Liste enthalten"
    print "0.99c ist %s-mal in der Liste enthalten" %(Preise.count(0.99))
    
    #Indizes herausfinden
    while i <= Preise.count(0.99):
        
        #Index herausfinden
        x = Preise.index(0.99, x)
        
        #ausgeben am Index
        print "%s: %s" %(x, Preise[x])
        
        #für nächsten Index vorbereiten
        x += 1
        
        #Zähler anpassen
        i += 1

#Zeichenkette leer anhängen
Preise.append("leer")

#Zähler zurücksetzen
i = 0
while i <= Preise.count(0.99):
    
    #aus der Liste entfernen
    Preise.remove(0.99)
    
    #Zähler anpassen
    i += 1

#Länge der Liste
print "\nLaenge der Liste: %s\n" %(len(Preise))

#Liste mit zwei multiplizieren
print "Preise *2\n%s \n" %(Preise * 2)

#Elemente verdoppeln
for Preis in Preise:
    NeuePreise.append(Preis*2)
Preise = NeuePreise

#Produkte Liste definieren
Produkte = ['Apfel','Banane','Birne']

#augeben einer Liste mit Preise + Produkte
print "Addition von Preise und Produkte: \n%s\n" %(Preise + Produkte)

#Liste Lager definieren
Lager = [Preise, Produkte]
print "Lager: \n%s \n" %(Lager)

#explizite Kopie machen
Lagerkopie = Lager[:]

#erster Test: hinzufügen eines Wertes
Lagerkopie.append('Tomate')
print "Lager nach dem ersten Test: \n%s \n" %(Lager)
print "explizite Kopie: \n%s \n" %(Lagerkopie)

#zweiter Test: herausnehmen eines Wertes
Lagerkopie.pop(1)
print "Lager nach dem zweiten Test: \n%s \n" %(Lager)
print "explizite Kopie: \n%s \n" %(Lagerkopie)