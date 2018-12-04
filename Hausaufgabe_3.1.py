# -*- coding: utf-8 -*-
"""
Name:Jesse Ziegler
Datum:02.11.2018

3. Hausaufgabe am 07.11.2018
"""

Briefe = {'163' : 4.2, '175' : 20.01, '214' : 15.5, '159' : 21.2}

schwerer = []
leichter = []

for Gewicht in Briefe:
    if Briefe[Gewicht] >= 20:
        schwerer.append(Gewicht)
    else:
        leichter.append(Gewicht)
print schwerer
print leichter


