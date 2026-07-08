"""
LÖSUNG 02: pytest-Testfälle (Black-Box, 5 Äquivalenzklassen)

Ausführen:  python3 -m pytest Loesungen/02_testen_pytest.py
"""

# import pytest   # nur nötig für pytest.raises(...) / @pytest.mark.xfail


def finde_groesste_gerade_zahl(zahlenliste):          # 🟩 vom Prof vorgegeben
    groesste = None
    for zahl in zahlenliste:
        if zahl % 2 == 0:
            if groesste is None or zahl > groesste:
                groesste = zahl
    if groesste is None:
        return "Keine gerade Zahl gefunden"
    return groesste


# 🟨 SELBST: ein Test pro Äquivalenzklasse
def test_k1_leere_liste():
    assert finde_groesste_gerade_zahl([]) == "Keine gerade Zahl gefunden"

def test_k2_nur_ungerade():
    assert finde_groesste_gerade_zahl([1, 3, 5, 7]) == "Keine gerade Zahl gefunden"

def test_k3_gemischt():
    assert finde_groesste_gerade_zahl([3, 7, 8, 2, 10, 5]) == 10

def test_k4_auch_negative():
    assert finde_groesste_gerade_zahl([-4, -2, -10, 3]) == -2

def test_k5_maximum_mehrfach():
    assert finde_groesste_gerade_zahl([4, 8, 8, 2]) == 8


# Ohne pytest zum schnellen Selbstcheck ausführbar:
if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_"):
            fn()
    print("Alle Tests grün.")
