"""
Übung 01: Defensive Assertions ergänzen (Testen, WS2526-Stil)

Gegeben ist die Funktion (inkl. der ersten assert-Zeile). Ergänze die
weiteren Assertions an der markierten Stelle.
"""


def normalize_and_pack(values, limit):
    assert type(values) == list                 # 🟩 vorgegeben

    # ✍️ SELBST: weitere defensive Assertions
    #   - limit muss eine ganze Zahl sein  -> isinstance(limit, int)
    #   - alle Elemente numerisch          -> all(isinstance(v, (int, float)) for v in values)

    # 🟩 ab hier vom Prof vorgegeben (evtl. mit Bug!)
    if limit < 0:
        raise ValueError("limit must be positive")
    cleaned = []
    for v in values:
        if v >= 0:
            cleaned.append(round(v))
    packs = [[]]
    for x in cleaned:
        if sum(packs[-1]) + x < limit:
            packs[-1].append(x)
        else:
            packs.append([x])
    if packs == [[]]:
        return []
    return packs


# Testaufrufe
print(normalize_and_pack([1, 2, 3], 10))     # erwartet: [[1, 2, 3]]
print(normalize_and_pack([-3, -1], 10))      # erwartet: []
# Nach dem Ergänzen sollte das hier einen AssertionError werfen:
# print(normalize_and_pack([1, 2], 10.5))
