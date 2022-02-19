#!/usr/bin/env python3
"""Module that contains unittests for decks."""

import unittest
import classes
from . import classes

"""
Deck = __import__('card_games/decks').Deck
PlayingCardDeck = __import__('card_games/decks').PlayingCardDeck
Hand = __import__('card_games/deck').Hand
Card = __import__('card_games/cards').Card
PlayingCard = __import__('card_games/cards').PlayingCard
"""

unopend_deck = ['A♣', '2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', '10♣',
                'J♣', 'Q♣', 'K♣', 'A♢', '2♢', '3♢', '4♢', '5♢', '6♢', '7♢',
                '8♢', '9♢', '10♢', 'J♢', 'Q♢', 'K♢', 'A♡', '2♡', '3♡', '4♡',
                '5♡', '6♡', '7♡', '8♡', '9♡', '10♡', 'J♡', 'Q♡', 'K♡', 'A♠',
                '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠',
                'Q♠','K♠']

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
temp = []
for suit in suits:
    for value in values:
        temp.append(PlayingCard(value, suit))
print(temp)