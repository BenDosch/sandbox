#!/usr/bin/env python3
"""Modules containing various classes of decks.
"""
# https://altcodeunicode.com/alt-codes-playing-card-symbols/

import random
from tkinter import N
PlayingCard = __import__('cards').PlayingCard


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

    def place(self, card, position: int=0) -> None:
        """Adds a card to the the deck at the specified position.

        Args:
            card (Card): A card to place on top of the deck.
            position (int): Location in the deck to draw from. Defaults to 0,
                the top.

        Returns: 
            1 on Sucess and None on failure.
        """
        if position >= len(self.cards) or position < (-1 * len(self.cards)):
            print("There are not that many cards in the deck.")
            return None

        self.cards.insert(position, card)
        return 1

    def shuffel(self):
        """Shuffles the deck, rearangeig the cards in a random order."""
        random.shuffle(self.cards)


    def __str__(self):
        """Reviels the cards in the deck."""
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
        if cards:
            self.cards = cards
        else:
            self.reset()

    def reset(self) -> None:
        """Returns all cards to the deck and shuffels it.
        """
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



class Hand(PlayingCardDeck):
    """A hand of cards"""

    def __init__(self) -> None:
        super().__init__()

    def card_from_deck(self, deck, position: int=0):
        """Draws a card from the specified deck.

        Args:
            deck (Deck): Deck to draw cards from.
            position (int, optional): Where in the deck to draw from. Defaults
                to the top.
        """
        self.cards.append(deck.draw(position))

    def card_to_deck(self, deck, card, position: int=0):
        """Places a card from the hand into a deck."""
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
        """Returns the hand to the default starting point. Empty"""
        self.cards = []

if __name__ == "__main__":
    deck = PlayingCardDeck()
    deck.show()
    print("Checkpoint 1 -------")
    print(deck.draw(0))
    print(deck.draw(-1))
    print("Checkpoint 2 -------")
    deck.show()
    deck.shuffel()
    print("Checkpoint 3 -------")
    deck.show()
    deck.place(card=PlayingCard("top", "test"), position=0)
    deck.place(card=PlayingCard("bottom", "test"), position=-1)
    deck.place(card=PlayingCard("to high", "test"), position=60)
    deck.place(card=PlayingCard("to low", "test"), position=-60)
    print("Checkpoint 4 -------")
    deck.show()
    print("======")
    deck.reset()
    deck.show()
    hand = Hand()
    hand.show()
    for i in range(5):
        hand.card_from_deck(deck)
    hand.show()
    deck.show()
    print("Checkpoint 5 -------")
    hand.sort_number()
    hand.show()
    hand.sort_suit()
    hand.show()
    print("Checkpoint 6 -------")
    hand.card_to_deck(deck, hand.cards[0])
    hand.show()
    deck.show()
    print("Checkpoint 7 -------")
    suits = ["♣", "♢", "♡", "♠"]
    values = ["A", "2", "3", "4", "5", "6", "7",
              "8", "9", "10", "J", "Q", "K"]
