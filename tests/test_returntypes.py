import pytest

from game.gamelogic import bot, botname, toss


def test_returnbot():
    assert type(bot()) == int


def test_returnbotname():
    ln = []
    assert type(botname(2, ln)) == type(None)


def test_returntoss():
    assert type(toss()) == int
