import sys
import pytest
import mock
import src.game as game


def test_convert_input_rock():
    assert game.convert_input('r') == 'rock'


def test_convert_input_paper():
    assert game.convert_input('p') == 'paper'


def test_convert_input_scissor():
    assert game.convert_input('s') == 'scissor'


def test_compare_input_rock_beat_scissor(capfd):
    game.compare_input('r', 's')
    out, err = capfd.readouterr()
    assert out == "\nUser has WON! User used rock to beat scissor\n\n"


def test_compare_input_paper_beat_rock(capfd):
    game.compare_input('p', 'r')
    out, err = capfd.readouterr()
    assert out == "\nUser has WON! User used paper to beat rock\n\n"


def test_compare_input_scissor_beat_paper(capfd):
    game.compare_input('s', 'p')
    out, err = capfd.readouterr()
    assert out == "\nUser has WON! User used scissor to beat paper\n\n"


def test_compare_input_scissor_lose_to_rock(capfd):
    game.compare_input('s', 'r')
    out, err = capfd.readouterr()
    assert out == "\nUser has LOST! Computer used rock to beat scissor\n\n"


def test_compare_input_rock_lose_to_paper(capfd):
    game.compare_input('r', 'p')
    out, err = capfd.readouterr()
    assert out == "\nUser has LOST! Computer used paper to beat rock\n\n"


def test_compare_input_paper_lose_to_scissor(capfd):
    game.compare_input('p', 's')
    out, err = capfd.readouterr()
    assert out == "\nUser has LOST! Computer used scissor to beat paper\n\n"


def test_compare_input_paper_ties_paper(capfd):
    game.compare_input('p', 'p')
    out, err = capfd.readouterr()
    assert out == "\nBoth user and the computer chose paper, so this round is a tie!\n\n"


def test_compare_input_scissor_ties_scissor(capfd):
    game.compare_input('s', 's')
    out, err = capfd.readouterr()
    assert out == "\nBoth user and the computer chose scissor, so this round is a tie!\n\n"


def test_compare_input_rock_ties_rock(capfd):
    game.compare_input('r', 'r')
    out, err = capfd.readouterr()
    assert out == "\nBoth user and the computer chose rock, so this round is a tie!\n\n"

