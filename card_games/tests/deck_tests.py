#!/usr/bin/env python3
"""Module that contains unittests for decks."""

import unittest
from unittest.mock import patch
from io import StringIO
from classes.decks import Deck
from classes.decks import PlayingCardDeck, PlayingCardHand
from classes.cards import PlayingCard


class TestPlayingCardClasses(unittest.TestCase):
    """Unittests for Playing Card related Classes."""

    @classmethod
    def setUpClass(self):
        """Class method that sets up variables for use by tests"""
        suits = ["♣", "♢", "♡", "♠"]
        values = ["A", "2", "3", "4", "5", "6", "7",
                  "8", "9", "10", "J", "Q", "K"]
        self.ordered_cards = []
        for suit in suits:
            for value in values:
                self.ordered_cards.append(PlayingCard(value, suit))

    def setUp(self) -> None:
        """Sets up before ever every test function is executed"""
        self.deck = PlayingCardDeck(self.ordered_cards)
        self.empty_deck = PlayingCardDeck([])
        self.hand = PlayingCardHand()

    def test_init(self):
        """"Tests of the __init__() functions."""
        # PlayingCardDeck
        with self.assertRaises(TypeError): 
            PlayingCardDeck("3♠")
        with self.assertRaises(TypeError): 
            PlayingCard(["4♠", "5♠"])
        random_deck1 = PlayingCardDeck()
        random_deck2 = PlayingCardDeck()
        self.assertEqual(52, len(random_deck1.cards))
        self.assertNotEqual(self.deck.cards, random_deck1)
        self.assertNotEqual(random_deck1.cards, random_deck2.cards)
        self.assertNotEqual(random_deck1.cards, random_deck2.cards)
        self.assertEqual(self.deck.cards, self.ordered_cards)
        self.assertTrue(all([isinstance(x, PlayingCard) for x in
                             self.deck.cards]))
        # Test all cards are unique
        card_list_1 = [card.name for card in random_deck1.cards]
        self.assertEqual(len(set(card_list_1)), len(card_list_1))

        # PlayingCardHand
        with self.assertRaises(TypeError):
            PlayingCardHand("3♠")
        with self.assertRaises(TypeError):
            PlayingCard(["4♠", "5♠"])
        ordered_hand = PlayingCardHand(self.ordered_cards)
        self.assertEqual(self.hand.cards, [])
        self.assertEqual(ordered_hand.cards, self.ordered_cards)
        self.assertTrue(all([isinstance(x, PlayingCard) for x in
                             ordered_hand.cards]))

    def test_str(self):
        """Tests for __str__ methods."""
        pass

    def test_show(self):
        """Tests for the show methods."""
        card_sample = self.deck.cards[0:3]

        # PlayingCardDeck
        deck = PlayingCardDeck(card_sample)
        with patch('sys.stdout', new = StringIO()) as fake_out:
            deck.show()
            check = '['
            for card in deck.cards:
                check += "'" + card.name + "', "
            check = check[:-2]
            check +=']\n'

            self.assertEqual(fake_out.getvalue(), check)

        # PlayingCardHand
        hand = PlayingCardHand(card_sample)
        with patch('sys.stdout', new = StringIO()) as fake_out:
            hand.show()
            check = '['
            for card in hand.cards:
                check += "'" + card.name + "', "
            check = check[:-2]
            check +=']\n'
            self.assertEqual(fake_out.getvalue(), check)

    def test_draw(self):
        """Tests for the draw methods"""
        card1 = self.ordered_cards[0]
        card2 = self.ordered_cards[-1]

        # PlayingCardDeck
        with self.assertRaises(TypeError):
            self.deck.draw("A♠")
        with self.assertRaises(TypeError):
            self.deck.draw([3, 5])
        with self.assertRaises(Exception):
            self.deck.draw(60)
        with self.assertRaises(Exception):
            self.deck.draw(-79)
        self.assertEqual(self.deck.draw(0), card1)
        self.assertEqual(self.deck.draw(-1), card2)

        # PlayingCardHand
        deck = PlayingCardDeck([card1, card2])
        with self.assertRaises(TypeError):
            self.hand.draw("deck", 0)
        with self.assertRaises(TypeError):
            self.hand.draw(deck, "A♠")
        with self.assertRaises(TypeError):
            self.hand.draw(deck, [3, 5])
        with self.assertRaises(Exception):
            self.hand.draw(deck, 60)
        with self.assertRaises(Exception):
            self.hand.draw(deck, -79)
        self.hand.draw(deck, 0)
        self.hand.draw(deck, -1)
        self.assertEqual(self.hand.cards[-2], card1)
        self.assertEqual(self.hand.cards[-1], card2)

    def test_shuffel(self):
        """Tests for the shuffel methods"""
        card_list = self.ordered_cards[0:5]

        # PlayingCardDeck
        deck1 = PlayingCardDeck(card_list)
        deck1.shuffel()
        self.assertEqual(len(deck1.cards), len(card_list))
        self.assertTrue(all(card in deck1.cards for card in card_list) and
                        all(card in card_list for card in deck1.cards))
        deck2 = PlayingCardDeck(card_list)
        self.assertNotEqual(deck1.__str__(), deck2.__str__())

        # PlayingCardHand
        hand = PlayingCardHand(card_list)
        hand.shuffel()
        self.assertEqual(len(hand.cards), len(card_list))
        self.assertTrue(all(card in hand.cards for card in card_list) and
                        all(card in card_list for card in hand.cards))
        self.assertNotEqual(hand.cards, card_list)

    def test_place(self):
        """Tests for the place methods"""

        card1 = self.ordered_cards[0]
        card2 = self.ordered_cards[-1]
        deck = Deck()

        # Deck
        with self.assertRaises(TypeError):
            deck.place("A♠", 0)
        with self.assertRaises(TypeError):
            deck.place(card1, 3, 5)
        with self.assertRaises(TypeError):
            deck.place(card1, [3, 5])
        with self.assertRaises(Exception):
            deck.place(card1, 60)
        with self.assertRaises(Exception):
            deck.place(card1, -79)
        deck.place(card1, 0)
        deck.place(card2,-1)
        self.assertEqual(deck.cards[0], card1)
        self.assertEqual(deck.cards[-1], card2)

        # PlayingCardHand
        deck = Deck()
        with self.assertRaises(TypeError):
            self.hand.place("deck", card1, 0)
        with self.assertRaises(TypeError):
            self.hand.place(deck, "A♠", 0)
        with self.assertRaises(TypeError):
            self.hand.place(deck, card1, 3, 5)
        with self.assertRaises(TypeError):
            self.hand.place(deck, card1, [3, 5])
        with self.assertRaises(Exception):
            self.hand.place(deck, card1, 60)
        with self.assertRaises(Exception):
            self.hand.place(deck, card1, -79)
        self.hand.place(deck, card1, 0)
        self.hand.place(deck, card2, -1)
        self.assertEqual(deck.cards[0], card1)
        self.assertEqual(deck.cards[-1], card2)

    def test_sorting(self):
        """Tests for the sorting methods"""
        # PlayingCardHand
        clubs = self.ordered_cards[0:2]
        dimonds = self.ordered_cards[13:15]
        sorted_suits = PlayingCardHand(clubs + dimonds)
        sorted_numbers = PlayingCardHand([dimonds[0], clubs[0],
                                          dimonds[1], clubs[1]])
        hand = PlayingCardHand(cards=dimonds + clubs)
        hand.sort_number()
        self.assertEqual(hand.__str__(), sorted_numbers.__str__())
        hand.sort_suit()
        self.assertEqual(hand.__str__(), sorted_suits.__str__())

    def test_reset(self):
        """Tests for the reset methods."""
        random_deck1 = PlayingCardDeck()
        random_deck2 = PlayingCardDeck()
        random_deck2.cards = random_deck1.cards
        random_deck1.reset()
        self.assertFalse(random_deck1.__str__() == random_deck2.__str__())

if __name__ == '__main__':
    unittest.main()