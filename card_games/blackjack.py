#!/usr/bin/env python3
"""Module that contains logic for the game blackjack."""

from classes.decks import PlayingCardDeck, PlayingCardHand


def new_round() -> tuple:
    """Sets up a new round of blackjack.

    Returns:
        tuple(PlayingCardDeck, PlayingCardHand, PlayingCardHand): Returns a
            randomized deck and hands with 2 cards for the player and dealer.
    """
    deck = PlayingCardDeck()
    player = PlayingCardHand()
    dealer = PlayingCardHand()

    for i in range(2):
        player.draw(deck, 0)
        dealer.draw(deck, 0)

    return (deck, player, dealer)


def calculate_score(hand: PlayingCardHand) -> tuple:
    """Function that calculates the score of PlayingCardHand in blackjack.

    Args:
        hand (PlayingCardHand): Hand of cards in blackjack.

    Returns:
        tuple(int, bool): Returns the score of the hand and True if there are
            unsued aces in the hand.
    """
    score = {"total": 0, "aces": 0}
    for card in hand.cards:
        if card.value in ["10", "J", "Q", "K"]:
            score["total"] += 10
        elif card.value == "A":
            score["total"] += 11
            score["aces"] += 1
        else:
            score["total"] += int(card.value)

    while score["total"] > 21 and score["aces"] > 0:
        score["total"] -= 10
        score["aces"] -= 1

    return (score["total"], True if score["aces"] >= 0 else False)


def player_turn(deck: PlayingCardDeck, hand: PlayingCardHand) -> int:
    """Conducts the player's turn in a round of blackjack.

    Args:
        deck (PlayingCardDeck): The deck used for the game.
        hand (PlayingCardHand): The players's hand.

    Returns:
        score(int): The final score for the players's hand.
    """
    score, _ = calculate_score(hand)

    while score < 21:
        print("Players has: " + str(score))
        hand.show()
        choice = input("Select an action by number. 1: Hit 2: Stay - ")

        if choice == "1":
            print("=== Hit ===")
            hand.draw(deck, 0)
        elif choice == "2":
            print("=== Stay at " + str(score) + " ===")
            score, _ = calculate_score(hand)
            break
        else:
            print("Please select 1 or 2.")
            continue

        score, _ = calculate_score(hand)

    return score


def dealer_turn(deck: PlayingCardDeck, hand: PlayingCardHand) -> int:
    """Conducts the dealer's turn in a round of blackjack.

    Args:
        deck (PlayingCardDeck): The deck used for the game.
        hand (PlayingCardHand): The dealer's hand.

    Returns:
        score(int): The final score for the dealer's hand.
    """
    score, _ = calculate_score(hand)
    print("Dealer has: " + str(score))
    hand.show()

    while score < 17:
        hand.draw(deck, 0)
        score, _ = calculate_score(hand)
        print("Dealer has: " + str(score))
        hand.show()

    return score


def main():
    """Main logic of the game."""
    # Set up game
    deck, player, dealer = new_round()
    print("Dealer is showing " + dealer.cards[1].name)
    # Player turn.
    player_score = player_turn(deck, player)
    # Check if player went bust
    if player_score > 21:
        print("Players has: " + str(player_score))
        player.show()
        print("Player Bust.")
        return
    # Dealer turn.
    dealer_score = dealer_turn(deck, dealer)
    if dealer_score > 21:
        print("Dealer Bust!")
        return

    # Calculate results.
    print("=========================")
    print("=====  Final Score  =====")
    print("=========================")
    print("Players has: " + str(player_score))
    player.show()
    print("Dealer has: " + str(dealer_score))
    dealer.show()

    if dealer_score >= player_score:
        print("Dealer Won.")
    else:
        print("Player Won!")

    return


if __name__ == "__main__":
    main()
