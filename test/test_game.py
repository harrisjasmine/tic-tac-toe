import unittest
import pytest
from unittest.mock import patch
from game.game import *


@pytest.fixture()
def board():
    return [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]


def test_if_selected_move_is_on_the_board(board):
    assert False == is_valid_move(-1, -1, board)
    assert True == is_valid_move(0, 0, board)
    assert True == is_valid_move(1, 1, board)
    assert False == is_valid_move(3, 0, board)
    assert False == is_valid_move(0, 3, board)
    assert False == is_valid_move(0, -1, board)


def test_can_somone_win_horizontally(board):
    board[0] = ['X', 'X', 'X']
    assert "winner is Jasmine" == check_if_player_won(board, "X", "Jasmine")


def test_can_someone_win_vertically(board):
    board[0][0] = 'X'
    board[1][0] = 'X'
    board[2][0] = 'X'
    assert "winner is Jasmine" == check_if_player_won(board, "X", "Jasmine")


def test_can_someone_win_descending_diagonally(board):
    board[0][0] = 'X'
    board[1][1] = 'X'
    board[2][2] = 'X'
    assert "winner is Jasmine" == check_if_player_won(board, "X", "Jasmine")


def test_can_someone_win_ascending_diagonally(board):
    board[0][2] = 'X'
    board[1][1] = 'X'
    board[2][0] = 'X'
    assert "winner is Jasmine" == check_if_player_won(board, "X", "Jasmine")

        
def test_play_again():
    with patch('builtins.input', return_value="yes") as mock_input:
        assert play_again() is True
    
    with patch('builtins.input', return_value="no") as mock_input:
        assert play_again() is False


@patch('builtins.input', side_effect=["Jasmine", "Kyle", "Lulu"])
def test_retrive_player_information(mock_input):
    expected = {1: {'name': 'Jasmine', 'character': 'X'}, 2: {'name': 'Kyle', 'character': 'O'}, 3: {'name': 'Lulu', 'character': 'A'}}
    assert expected == retrieve_player_information(3)


def test_draw():
    board = [['X', 'O', 'X'], ['X', 'O', 'X'], ['O', 'X', 'O']]
    assert "no winner, draw game" == check_if_player_won(board, "X", "Jasmine")


def test_clean_up_coordinates():
    coordinates = "          1,      2"
    assert 1, 2 == clean_up_coordinates(coordinates)


if __name__ == '__main__':
    unittest.main()