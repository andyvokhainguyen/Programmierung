"""
LÖSUNG 07: Exception Handling try/except/else/finally
"""


def teile_wert(liste, index, teiler):
    try:
        wert = liste[index]              # kann IndexError werfen
        zahl = int(teiler)               # kann ValueError werfen
        ergebnis = wert / zahl           # kann ZeroDivisionError werfen
    except IndexError:
        print("Fehler: Index ausserhalb der Liste.")
    except ValueError:
        print("Fehler: keine gültige Zahl.")
    except ZeroDivisionError:
        print("Fehler: Division durch Null.")
    else:
        print("Ergebnis:", ergebnis)     # nur wenn KEIN Fehler
        return ergebnis
    finally:
        print("Berechnung abgeschlossen.")   # IMMER


teile_wert([10, 20, 30], 1, "2")     # Ergebnis: 10.0 + abgeschlossen
teile_wert([10, 20, 30], 5, "2")     # Index-Fehler + abgeschlossen
teile_wert([10, 20, 30], 1, "0")     # Division durch Null + abgeschlossen
teile_wert([10, 20, 30], 1, "x")     # keine gültige Zahl + abgeschlossen
