#!/usr/bin/env python3
"""Modules containing various classes of cards.
"""
# https://altcodeunicode.com/alt-codes-playing-card-symbols/


class Card():
    """Base class for varius types of cards."""

    def __init__(self) -> None:
        pass


class PlayingCard(Card):
    """Class that represents cards from a standard 52 card 4 suit playing card
    deck."""

    def __init__(self, value: str, suit: str) -> None:
        super().__init__()
        self.value = value
        self.suit = suit

    def __str__(self):
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
