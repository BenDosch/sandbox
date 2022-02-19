#!/usr/bin/env python3
"""Modules containing various classes of decks."""

import random
from card_games.classes.cards import Card, PlayingCard


class Deck():
    """Base class for decks of various games."""

    def __init__(self) -> None:
        """Generate new deck"""
        self.cards = []

    def draw(self, position: int=0):
        """Removes the a card from self.cards at the given postion and
        returns it.

        Args:
            position (int): Location in the deck to draw from. Defaults to 0,
                the top.

        Returns: Card or None on failure.
            Card: The card in the sepecified position from the deck.
        """
        if position >= len(self.cards) or position < (-1 * len(self.cards)):
            print("There are not that many cards in the deck.")
            return None

        return self.cards.pop(position)

    def place(self, card: Card, position: int=0) -> None:
        """Adds a card to the the deck at the specified position.

        Args:
            card (Card): A card to place on top of the deck.
            position (int): Location in the deck to draw from. Defaults to 0,
                the top.
        """
        if not isinstance(card, Card):
            raise TypeError("card must be a type of Card object.")
        if not isinstance(position, int):
            raise TypeError("position must be an int.")

        if position >= len(self.cards) or position < (-1 * len(self.cards)):
            raise Exception("There are not that many cards in the deck.")

        self.cards.insert(position, card)

    def shuffel(self):
        """Shuffles the deck, rearangeig the cards in a random order."""
        random.shuffle(self.cards)

    def __str__(self):
        """Sets the string representation of the deck to the cards inside."""
        string = ""

        for card in self.cards:
            if string != "":
                string += ", " + card.name
            else:
                string = card.name

        return string


class PlayingCardDeck(Deck):
    """A deck of playing cards."""

    def __init__(self, cards: list=None) -> None:
        super().__init__()
        if not isinstance(cards, list):
            raise TypeError("cards must be a list")
        if not all([isinstance(x, Card) for x in cards]):
            raise TypeError("All objects in cards must be Card objects.")

        if cards:
            self.cards = cards
        else:
            self.reset()

    def reset(self) -> None:
        """Returns all cards to the deck and shuffels it."""
        self.cards.clear()

        suits = ["♣", "♢", "♡", "♠"]
        values = ["A", "2", "3", "4", "5", "6", "7",
                  "8", "9", "10", "J", "Q", "K"]
        for suit in suits:
            for value in values:
                self.cards.append(PlayingCard(value, suit))

        self.shuffel()

    def show(self):
        """Shows the playing cards in deck."""
        print(type(self.cards))
        print([card.name for card in self.cards])



class PlayingCardHand(PlayingCardDeck):
    """A hand of playing cards"""

    def __init__(self, cards: list=None) -> None:
        super().__init__()
        if not isinstance(cards, list):
            raise TypeError("cards must be a list")
        if not all([isinstance(x, Card) for x in cards]):
            raise TypeError("All objects in cards must be Card objects.")

        if cards:
            self.cards = cards
        else:
            self.cards = []

    def draw(self, deck: Deck, position: int=0):
        """Draws a card from the specified deck.

        Args:
            deck (Deck): Deck to draw cards from.
            position (int, optional): Where in the deck to draw from. Defaults
                to the top.
        """
        if not isinstance(deck, Deck):
            raise TypeError("deck must be a Deck object")
        if not isinstance(position, int):
            raise TypeError("position must be an int.")

        self.cards.append(deck.draw(position))

    def place(self, deck: Deck, card: Card, position: int=0):
        """Places a card from the hand into a deck."""
        if not isinstance(deck, Deck):
            raise TypeError("deck must be a Deck object.")
        if not isinstance(card, Card):
            raise TypeError("card must be a Card object.")
        if not isinstance(position, int):
            raise TypeError("position must be an int.")

        if card in self.cards:
            self.cards.remove(card)
            deck.place(card, position)
        else:
            print("Card was not in hand.")

    def sort_number(self):
        """Sorts hand by number."""
        self.cards.sort()

    def sort_suit(self):
        """sorts hand by suit"""
        temp = []
        self.cards.sort()
        suits = ["♣", "♢", "♡", "♠"]
        [[temp.append(card) for card in self.cards if suit in card.name]
         for suit in suits]
        self.cards = temp

    def reset(self):
        """Returns the hand to the default starting point of empty"""
        self.cards = []

if __name__ == "__main__":
    pass
