import unittest



def test_is_valid():
    assertEqual(False, is_valid(-1, -1))
    assertEqual(True, is_valid(0, 0))
    assertEqual(True, is_valid(1, 1))
    assertEqual(False, is_valid(3, 0))
    assertEqual(False, is_valid(0, 3))
    assertEqual(False, is_valid(0, -1))


def test_draw_board()