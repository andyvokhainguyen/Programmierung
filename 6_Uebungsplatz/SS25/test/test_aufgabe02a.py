"""
Aufgabe 2a - Klausur Programmierung
"""

from src import aufgabe02a

import pytest

def test_finde_groesste_gerade_zahl_gemischt():
    # K1 Normallfall
    assert aufgabe02a.finde_groesste_gerade_zahl([3, 7, 8, 2, 10, 5]) == 10

def test_finde_groesste_gerade_zahl_leere_liste():
    # K2 Leere Liste
    assert aufgabe02a.finde_groesste_gerade_zahl([]) == "Keine gerade Zahl gefunden"

def test_finde_groesste_gerade_zahl_keine():
    # K3 Nur ungerade Zahlen
    assert aufgabe02a.finde_groesste_gerade_zahl([1, 3, 5, 7, 9]) == "Keine gerade Zahl gefunden"

def test_finde_groesste_gerade_zahl_negativ():
    # K4 Größte Zahl negativ
    assert aufgabe02a.finde_groesste_gerade_zahl([-4, -2, -10, 3]) == -2

def test_finde_groesste_gerade_zahl_mehrfach():
    # K5 Größte Zahl mehrfach vorhanden
    assert aufgabe02a.finde_groesste_gerade_zahl([4, 8, 8, 2]) == 8