import unittest
import pytest
from game.game import *

@pytest.fixture()
def board():
    return [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]


def test_if_selected_move_is_on_the_board(board):
    assert False == is_valid(-1, -1, board)
    assert True == is_valid(0, 0, board)
    assert True == is_valid(1, 1, board)
    assert False == is_valid(3, 0, board)
    assert False == is_valid(0, 3, board)
    assert False == is_valid(0, -1, board)


def test_can_somone_win_horizontally(board):
    board[0] = ['X', 'X', 'X']
    assert "winner is X" == check_if_player_won(board, "X")


def test_can_someone_win_vertically(board):
    board[0][0] = 'X'
    board[1][0] = 'X'
    board[2][0] = 'X'
    assert "winner is X" == check_if_player_won(board, "X")


def test_can_someone_win_descending_diagonally(board):
    board[0][0] = 'X'
    board[1][1] = 'X'
    board[2][2] = 'X'
    assert "winner is X" == check_if_player_won(board, "X")


def test_can_someone_win_ascending_diagonally(board):
    board[0][2] = 'X'
    board[1][1] = 'X'
    board[2][0] = 'X'
    assert "winner is X" == check_if_player_won(board, "X")


# def test_can_a_player_override_another_player(board):
#     board[0][0] = 'X'
    

def test_retrive_player_information():
    pass


def test_draw():
    board = [['X', 'O', 'X'], ['X', 'O', 'X'], ['O', 'X', 'O']]
    assert "no winner, draw game" == check_if_player_won(board, "X")


def test_clean_up_coordinates():
    coordinates = "          1,      2"
    assert 1, 2 == clean_up_coordinates(coordinates)


if __name__ == '__main__':
    unittest.main()