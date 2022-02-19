#!/usr/bin/env python3
"""Modules containing various classes of cards."""


class Card():
    """Base class for varius types of cards."""

    def __init__(self) -> None:
        pass


class PlayingCard(Card):
    """Class that represents cards from a standard 52 card 4 suit playing card
    deck."""

    def __init__(self, value: str, suit: str) -> None:
        """Initialize an object representing a playing card basied on a given
        value and suit.

        Args:
            value (str): Value of the card, A, 1-10, J, Q, or K.
            suit (str): The suit of the card, Clubs, Dimonds, Hearts or Spade,
                represented byt the symbols ♣, ♢, ♡, or ♠ respectively.
        """
        super().__init__()
        if not isinstance(value, str):
            raise TypeError("value must be a string")
        if value not in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10",
                         "J", "Q", "K"]:
            raise ValueError("value must be A, 2, 3, 4, 5, 6, 7, 8, 9, 10," + 
                             " J, Q, or K")
        if not isinstance(suit, str):
            raise TypeError("suit must be a string.")
        if suit not in ["♣", "♢", "♡", "♠"]:
            raise ValueError("suit must be ♣, ♢, ♡, or ♠")
        self.value = value
        self.suit = suit

    def __str__(self):
        """Changes the string representation of the"""
        return self.name

    def __lt__(self, other):
        """Redefines the behavior of the < opperator"""
        return self.name < other.name
        
    def __le__(self, other):
        """Redefines the behavior of the <= opperator"""
        return self.name <= other.name

    def __eq__(self, other):
        """Redefines the behavior of the == opperator"""
        return self.name == other.name

    def __ne__(self, other):
        """Redefines the behavior of the != opperator"""
        return self.name != other.name
        
    def __gt__(self, other):
        """Redefines the behavior of the > opperator"""
        return self.name > other.name
        
    def __ge__(self, other):
        """Redefines the behavior of >= opperator"""
        return self.name >= other.name

    @property
    def name(self):
        """Returns the combined value and suit of the card."""
        return self.value + self.suit
