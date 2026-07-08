"""
Übung 02: pytest-Testfälle schreiben (Testen, Black-Box)

Gegeben: die zu testende Funktion (vom Prof). Selbst: pro Äquivalenzklasse
einen Test schreiben.

Ausführen:  python3 -m pytest 02_testen_pytest.py
(In der echten Klausur liegt die Funktion in src/, Import: `from src import aufgabe02`.)
"""

# import pytest   # nur nötig für pytest.raises(...) oder @pytest.mark.xfail


def finde_groesste_gerade_zahl(zahlenliste):          # 🟩 vom Prof vorgegeben
    groesste = None
    for zahl in zahlenliste:
        if zahl % 2 == 0:
            if groesste is None or zahl > groesste:
                groesste = zahl
    if groesste is None:
        return "Keine gerade Zahl gefunden"
    return groesste


# ✍️ SELBST: pro Äquivalenzklasse GENAU EIN Test (Name muss mit test_ beginnen):
#   K1 leere Liste       []            -> "Keine gerade Zahl gefunden"
#   K2 nur ungerade      [1,3,5,7]     -> "Keine gerade Zahl gefunden"
#   K3 gemischt          [3,7,8,2,10]  -> 10
#   K4 auch negative     [-4,-2,-10,3] -> -2   (Achtung: -2, nicht -10!)
#   K5 Maximum mehrfach  [4,8,8,2]     -> 8

def test_k1_leere_liste():
    assert finde_groesste_gerade_zahl([]) == "Keine gerade Zahl gefunden"

def test_k1_ungerade():
    assert finde_groesste_gerade_zahl([1, 3, 5, 7]) == "Keine gerade Zahl gefunden"

def test_k1_gemischt():
    assert finde_groesste_gerade_zahl([3, 7, 8, 2, 10]) == 10

def test_k1_negativ():
    assert finde_groesste_gerade_zahl([-4, -2, -10, 3]) == -2

def test_k1_max():
    assert finde_groesste_gerade_zahl([4, 8, 8, 2]) == 8

# ✍️ SELBST: test_k2 ... test_k5 hier ergänzen
