#!/usr/bin/env python3
"""Module that contains unittests for decks."""

import unittest
from classes.cards import PlayingCard


class TestPlayingCardClasses(unittest.TestCase):
    """Unittests for Playing Card related Classes."""

    def setUpClass(self):
        """Class method that sets up variables for use by tests"""
        pass

    def setUp(self) -> None:
        """Sets up before ever every test function is executed"""
        pass

    def test_init(self):
        """"Tests of the __init__() functions."""
        # PlayingCard
        self.assertRaises(Exception, PlayingCard())
        self.assertRaises(Exception, PlayingCard("1"))
        self.assertRaises(Exception, PlayingCard("1", "♠", "extra"))
        self.assertRaises(TypeError, PlayingCard(["1"], "♠"))
        self.assertRaises(TypeError, PlayingCard("1", 1))
        self.assertRaises(ValueError, PlayingCard("1", "4"))
        self.assertRaises(ValueError, PlayingCard("1", "club"))
        self.assertRaises(ValueError, PlayingCard("♢", "♢"))
        self.assertRaises(ValueError, PlayingCard("0", "♣"))
        card1 = PlayingCard("9", "♣")
        self.assertEqual(card1.value, "9")
        self.assertEqual(card1.suit, "♣")
        self.assertEqual(card1.name, "9♣")
        card2 = PlayingCard("A", "♠")
        self.assertEqual(card1.value, "A")
        self.assertEqual(card1.suit, "♠")
        self.assertEqual(card1.name, "A♠")

    def test_operators(self):
        """Tests for changes to operators."""
        pass

    def test_(self):
        """Test template"""
        pass
