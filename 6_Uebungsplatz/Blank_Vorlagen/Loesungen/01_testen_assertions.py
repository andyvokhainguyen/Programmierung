"""
LÖSUNG 01: Defensive Assertions ergänzen
"""


def normalize_and_pack(values, limit):
    assert type(values) == list                              # 🟩 vorgegeben
    # 🟨 SELBST ergänzt:
    assert isinstance(limit, int), "limit muss eine ganze Zahl sein"
    assert all(isinstance(v, (int, float)) for v in values), \
        "alle Elemente von values muessen int oder float sein"

    # 🟩 vorgegeben
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


print(normalize_and_pack([1, 2, 3], 10))     # [[1, 2, 3]]
print(normalize_and_pack([-3, -1], 10))      # []
try:
    normalize_and_pack([1, 2], 10.5)
except AssertionError as e:
    print("AssertionError:", e)              # -> greift, weil limit kein int
