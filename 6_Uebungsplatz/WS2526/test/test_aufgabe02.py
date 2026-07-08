"""
Aufgabe 2e - Klausur Programmierung WS2025/26
"""

import pytest

from src import aufgabe02a


def test_normalize_and_pack():
    assert aufgabe02a.normalize_and_pack([1, 2, 3], 10) == [[1, 2, 3]]
