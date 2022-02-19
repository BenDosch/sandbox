#!/usr/bin/env python3
"""Module that contains unittests for decks."""

import unittest
from unittest.mock import patch
from io import StringIO
from card_games.classes.decks import Deck
from classes.decks import PlayingCardDeck, PlayingCardHand
from classes.cards import PlayingCard


class TestPlayingCardClasses(unittest.TestCase):
    """Unittests for Playing Card related Classes."""

    def setUpClass(self):
        """Class method that sets up variables for use by tests"""
        suits = ["♣", "♢", "♡", "♠"]
        values = ["A", "2", "3", "4", "5", "6", "7",
                  "8", "9", "10", "J", "Q", "K"]
        self.ordered_cards = []
        for suit in suits:
            for value in values:
                self.ordered_cards.append(PlayingCard(value, suit))

        self.unopened_deck = PlayingCardDeck(self.ordered_cards)

    def setUp(self) -> None:
        """Sets up before ever every test function is executed"""
        deck = PlayingCardDeck(self.unopened_deck)
        empty_deck = PlayingCardDeck(self.empty_deck)
        hand = PlayingCardHand()

    def test_init(self):
        """"Tests of the __init__() functions."""
        # PlayingCardDeck
        self.assertRaises(TypeError, PlayingCardDeck("3♠"))
        self.assertRaises(TypeError, PlayingCard(["4♠", "5♠"]))
        random_deck1 = PlayingCardDeck()
        random_deck2 = PlayingCardDeck()
        self.assertEqual(52, len(random_deck1.cards))
        self.assertNotEqual(self.unopened_deck.cards, random_deck1)
        self.assertNotEqual(random_deck1.cards, random_deck2.cards)
        self.assertNotEqual(random_deck1.cards, random_deck2.cards)
        self.assertEqual(self.deck.cards, self.ordered_cards)
        self.assertTrue(all([isinstance(x, PlayingCard) for x in
                             self.deck.cards]))
        # Test all cards are unique
        card_list_1 = [card.name for card in random_deck1.cards]
        self.assertEqual(len(set(card_list_1)) == len(card_list_1))
        

        # PlayingCardHand
        self.assertRaises(TypeError, PlayingCardHand("3♠"))
        self.assertRaises(TypeError, PlayingCard(["4♠", "5♠"]))
        random_hand1 = PlayingCardHand()
        random_hand2 = PlayingCardHand()
        self.assertNotEqual(self.unopened_hand.cards, random_hand1)
        self.assertNotEqual(random_hand1.cards, random_hand2.cards)
        self.assertNotEqual(random_hand1.cards, random_hand2.cards)
        self.assertEqual(self.hand.cards, self.ordered_cards)
        self.assertTrue(all([isinstance(x, PlayingCard) for x in
                             self.hand.cards]))

    def test_str(self):
        """Tests for __str__ methods."""
        pass

    def test_show(self):
        """Tests for the show methods."""
        card_sample = self.unopened_deck.cards[0:3]
        
        # PlayingCardDeck
        deck = PlayingCardDeck(card_sample)
        with patch('sys.stdout', new = StringIO()) as fake_out:
            self.deck.show()
            self.assertEqual(fake_out.getvalue(), str(card_sample))

        # PlayingCardHand
        hand = PlayingCardHand(card_sample)
        with patch('sys.stdout', new = StringIO()) as fake_out:
            self.hand.show()
            self.assertEqual(fake_out.getvalue(), str(card_sample))

    def test_draw(self):
        """Tests for the draw methods"""
        card1 = self.ordered_cards[0]
        card2 = self.ordered_cards[-1]

        # PlayingCardDeck
        self.assertRaises(TypeError, self.deck.draw("A♠"))
        self.assertRaises(TypeError, self.deck.draw([3, 5]))
        self.assertRaises(Exception, self.deck.draw(60))
        self.assertRaises(Exception, self.deck.draw(-79))
        self.assertEqual(self.deck.draw(0), card1)
        self.assertEqual(self.deck.draw(-1), card2)

        # PlayingCardHand
        deck = PlayingCardDeck([card1, card2])
        self.assertRaises(TypeError, self.hand.draw("deck", 0))
        self.assertRaises(TypeError, self.hand.draw(deck, "A♠"))
        self.assertRaises(TypeError, self.hand.draw(deck, [3, 5]))
        self.assertRaises(Exception, self.hand.draw(deck, 60))
        self.assertRaises(Exception, self.hand.draw(deck, -79))
        self.assertEqual(self.hand.draw(deck, 0), card1)
        self.assertEqual(self.hand.draw(deck, -1), card2)

    def test_shuffel(self):
        """Tests for the shuffel methods"""
        card_list = self.ordered_cards[0:5]

        # PlayingCardDeck
        deck = PlayingCardDeck(card_list)
        deck.shuffel()
        self.assertEqual(len(deck.cards), len(card_list))
        self.assertTrue(all(card in deck.cards for card in card_list) and
                        all(card in card_list for card in deck.cards))
        self.assertNotEqual(deck.cards, card_list)

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
        self.assertRaises(TypeError, deck.place("A♠", 0))
        self.assertRaises(TypeError, deck.place(card1, 3, 5))
        self.assertRaises(TypeError, deck.place(card1, [3, 5]))
        self.assertRaises(Exception, deck.place(card1, 60))
        self.assertRaises(Exception, deck.place(card1, -79))
        deck.place(card1, 0)
        deck.place(card2,-1)
        self.assertEqual(deck.cards[0], card1)
        self.assertEqual(deck.cards[-1], card2)

        # PlayingCardHand
        deck = Deck()
        self.assertRaises(TypeError, self.hand.place("deck", card1, 0))
        self.assertRaises(TypeError, self.hand.place(deck, "A♠", 0))
        self.assertRaises(TypeError, self.hand.place(deck, card1, 3, 5))
        self.assertRaises(TypeError, self.hand.place(deck, card1, [3, 5]))
        self.assertRaises(Exception, self.hand.place(deck, card1, 60))
        self.assertRaises(Exception, self.hand.place(deck, card1, -79))
        self.hand.place(deck, card1, 0)
        self.hand.place(deck, card2, -1)
        self.assertEqual(deck.cards[0], card1)
        self.assertEqual(deck.cards[-1], card2)
    
    def test_sorting(self):
        """Tests for the sorting methods"""
        # PlayingCardHand
        clubs = self.ordered_cards[0:2]
        dimonds = self.ordered_cards[13:15]
        sorted_suits = clubs + dimonds
        sorted_numbers = [clubs[0], dimonds[0], clubs[1], dimonds[1]]
        hand = PlayingCardHand([dimonds + clubs])
        self.assertEqual(hand.sort_number(), sorted_numbers)
        self.assertEqual(hand.sort_suit(), sorted_suits)

    def test_reset(self):
        """Tests for the reset methods."""
        random_deck1 = PlayingCardDeck()
        random_deck2 = PlayingCardDeck()
        random_deck2.cards = random_deck1.cards
        random_deck1.reset()
        self.assertNotEqual(random_deck1.cards, random_deck2.cards)

    def test_(self):
        """Test template"""
        pass
