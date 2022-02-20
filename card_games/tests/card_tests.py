#!/usr/bin/env python3
"""Module that contains unittests for decks."""

import unittest
from classes.cards import PlayingCard


class TestPlayingCardClasses(unittest.TestCase):
    """Unittests for Playing Card related Classes."""

    @classmethod
    def setUpClass(self):
        """Class method that sets up variables for use by tests"""
        pass

    def setUp(self) -> None:
        """Sets up before ever every test function is executed"""
        pass

    def test_init(self):
        """"Tests of the __init__() functions."""
        # PlayingCard
        with self.assertRaises(Exception):
            PlayingCard()
        with self.assertRaises(Exception):
            PlayingCard("2")
        with self.assertRaises(Exception):
            PlayingCard("2", "♠", "extra")
        with self.assertRaises(TypeError):
            PlayingCard(["2"], "♠")
        with self.assertRaises(TypeError):
            PlayingCard("2", 2)
        with self.assertRaises(ValueError):
            PlayingCard("2", "4")
        with self.assertRaises(ValueError):
            PlayingCard("2", "club")
        with self.assertRaises(ValueError):
            PlayingCard("♢", "♢")
        with self.assertRaises(ValueError):
            PlayingCard("0", "♣")
        card1 = PlayingCard("9", "♣")
        self.assertEqual(card1.value, "9")
        self.assertEqual(card1.suit, "♣")
        self.assertEqual(card1.name, "9♣")
        card2 = PlayingCard("A", "♠")
        self.assertEqual(card2.value, "A")
        self.assertEqual(card2.suit, "♠")
        self.assertEqual(card2.name, "A♠")

    def test_operators(self):
        """Tests for changes to operators."""
        pass

    def test_(self):
        """Test template"""
        pass
