"""
Aufgabe 2b - Klausur Programmierung
"""

from src import aufgabe02b

import pytest

def test_schnittmenge_gemischt():
    # P1 Abwechselnd Treffer und Nicht Treffer
    assert aufgabe02b.schnittmenge([1, 2, 3], [2, 4]) == [2]

def test_schnittmenge_leere_menge1():
    # P2 Basisfall, menge1 leer
    assert aufgabe02b.schnittmenge([], [1, 2, 3]) == []

def test_schnittmenge_alle_gemeinsam():
    # P3 menge1 und menge2 stimmen überein
    assert aufgabe02b.schnittmenge([1, 2], [1, 2]) == [1, 2]

def test_schnittmenge_keine():
    # P4 Keine gemeinsame Schnittmenge
    assert aufgabe02b.schnittmenge([1, 2, 3], [4, 5]) == []

def test_schnittmenge_leere_menge2():
    # P5 menge2 leer
    assert aufgabe02b.schnittmenge([1, 2, 3], []) == []

def test_schnittmenge_mehrfach():
    # P6 Mehrfachvorkommen
    assert aufgabe02b.schnittmenge([2, 2, 3], [2]) == [2, 2]
