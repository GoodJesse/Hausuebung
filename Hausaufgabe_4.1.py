# -*- coding: utf-8 -*-
"""
Name:Jesse Ziegler
Datum:22.10.2018

4. Hausaufgabe am 31.10.2018
"""

#Funktion definieren mit einem Dict und einem String als Parameter
def Bearbeitung(Dict, String):
	#String verdoppeln
	String *= 2
	
	#doppelten String in Woerterbuch
	Dict['doppelt'] = String
	
	print "\nAusgabe aus der Funktion"
	print "Dict: ", Dict, "\nString: ", String

#Variablen definieren
Dict_main = {"Buch" : 0.2, "Kekse" : 0.3}
string_main = "Buch"

#Funktion aufrufen
Bearbeitung(Dict_main, string_main)

print "\nAusgabe aus dem Hauptcode"
print "Dict: ", Dict_main, "\nString: ", string_main

"""
Dictionary hat sich veraendert, String nicht
Dictionaries sind veraenderlich und daher call by reference (Es wird das ganze Objekt uebergeben)
Strings sind unveraenderlich, also call by value (Nur der Wert wird der Funktion uebergeben)
"""

#Funktion welche dict nicht veraendert definieren
def Bearbeitung_Kopie(Dict, String):
	
	#String verdoppeln
	String *= 2
	
	#doppelten String in Woerterbuch
	Dict_copy = Dict.copy()
	Dict_copy['doppelt'] = String
	
	print "\nAusgabe aus der Funktions-Kopie"
	print "Dict: ", Dict, "\nString: ", String, "\nDict_Kopie: ", Dict_copy

#Variablen definieren
Dict_main = {"Buch" : 0.2, "Kekse" : 0.3}
string_main = "Buch"

#Funktion ausrufen
Bearbeitung_Kopie(Dict_main, string_main)

print "\nAusgabe aus dem Hauptcode-Kopie"
print "Dict: ", Dict_main, "\nString: ", string_main

#Dict verändert sich nicht