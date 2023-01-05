# ############## Blackjack Project #####################

# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

# ############## Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

# #################### Hints #####################

# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

import os
import random
import time


def hit_act(all_cards, cards, score):
    cards.append(all_cards[random.randint(0, 12)])
    score = sum(cards)
    if score > 21:
        for i in range(len(cards)):
            if cards[i] == 11:
                cards[i] = 1
                score -= 10
                break
    return score


def print_act(print_cards, cards):
    print_cards = cards[:]
    for i in range(len(print_cards)):
        if print_cards[i] in [1, 11]:
            print_cards[i] = "A"
    return print_cards


def check_act(player_score, dealer_score, money_dic, deal_act):
    if player_score > 21:
        _extracted_from_check_act_lose(money_dic, deal_act)
        return
    elif dealer_score > 21:
        _extracted_from_check_act_win(money_dic, deal_act)
        return
    else:
        if player_score > dealer_score:
            _extracted_from_check_act_win(money_dic, deal_act)
        elif player_score < dealer_score:
            _extracted_from_check_act_lose(money_dic, deal_act)
        else:
            print("Draw!")


# TODO Rename this here and in `check_act`
def _extracted_from_check_act_win(money_dic, deal_act):
    print(f"YOU WIN ${deal_act}!")
    money_dic["player"] += deal_act
    money_dic["dealer"] -= deal_act


# TODO Rename this here and in `check_act`
def _extracted_from_check_act_lose(money_dic, deal_act):
    print(f"YOU LOSE ${deal_act}!")
    money_dic["player"] -= deal_act
    money_dic["dealer"] += deal_act


# initial variables
player_cards = []
dealer_cards = []
player_print_cards = []
dealer_print_cards = []
player_score = 0
dealer_score = 0
all_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
money_dic = {
    "player": 1000,
    "dealer": 1000,
}
deal_act = 0
print(f"Your money: {money_dic['player']}\n")
print(f"dealer_money: {money_dic['dealer']}\n")
dealer_cards_amount = 0
is_continue = False
is_again = False

while not is_again:
    # clear
    os.system("cls")

    # deal set
    deal_act = int(input("How much money do you want to deal?\n"))

    while not is_continue:
        # start to play
        player_act = input("choice! hit, stand, double\n")

        if player_act == "hit":
            # player hit the card
            print(f"You choice {player_act}!\n")
            player_score = hit_act(all_cards,
                                   cards=player_cards,
                                   score=player_score)
            player_print_cards = print_act(print_cards=player_print_cards,
                                           cards=player_cards)
            print(
                f"Your print cards:{player_print_cards}\nYour cards:{player_cards}\nYour score: {player_score}\n\n"
            )
            if player_score > 21:
                break
            # if players score more than dealer score, then dealer choice hit too
            if dealer_score < player_score or dealer_score <= 16:
                dealer_cards_amount += 1
                print("Dealer also choice hit!\n")
                dealer_score = hit_act(all_cards,
                                       cards=dealer_cards,
                                       score=dealer_cards)
            else:
                print("Dealer choice stand!\n")
            dealer_print_cards = print_act(print_cards=dealer_print_cards,
                                           cards=dealer_cards)
            print(
                f"Dealer first cards:{dealer_print_cards[0]}\nDealer cards: {dealer_cards}\nDealer score: {dealer_score}\nDealer got {dealer_cards_amount} cards\n\n"
            )
        elif player_act == "stand":
            # player stand
            print(f"You choice {player_act}!\n")
            print(
                f"Your print cards:{player_print_cards}\nYour cards:{player_cards}\nYour score: {player_score}\n\n"
            )
            is_continue = True
            # if players score more than dealer score, then dealer choice hit too
            while dealer_score < player_score or dealer_score <= 16:
                dealer_cards_amount += 1
                print("Dealer also choice hit!\n")
                dealer_score = hit_act(all_cards,
                                       cards=dealer_cards,
                                       score=dealer_cards)
                dealer_print_cards = print_act(print_cards=dealer_print_cards,
                                               cards=dealer_cards)
                print(
                    f"Dealer first cards:{dealer_print_cards[0]}\nDealer cards: {dealer_cards}\nDealer score: {dealer_score}\nDealer got {dealer_cards_amount} cards\n\n"
                )
                time.sleep(2)
        else:
            # player double
            deal_act *= 2
            player_score = hit_act(all_cards,
                                   cards=player_cards,
                                   score=player_score)
            player_print_cards = print_act(print_cards=player_print_cards,
                                           cards=player_cards)
            print(
                f"Your print cards:{player_print_cards}\nYour cards:{player_cards}\nYour score: {player_score}\n\n"
            )
            if player_score > 21:
                break
            is_continue = True
            while dealer_score < player_score or dealer_score <= 16:
                dealer_cards_amount += 1
                print("Dealer also choice hit!\n")
                dealer_score = hit_act(all_cards,
                                       cards=dealer_cards,
                                       score=dealer_cards)
                dealer_print_cards = print_act(print_cards=dealer_print_cards,
                                               cards=dealer_cards)
                print(
                    f"Dealer first cards:{dealer_print_cards[0]}\nDealer cards: {dealer_cards}\nDealer score: {dealer_score}\nDealer got {dealer_cards_amount} cards\n\n"
                )
                time.sleep(2)

    check_act(player_score, dealer_score, money_dic, deal_act)
    print(f"Your money: {money_dic['player']}\n")
    print(f"dealer_money: {money_dic['dealer']}\n")
    if money_dic['player'] <= 0:
        print("Congratulations,you defeat Dealer. Thanks for playing!")
        break
    elif money_dic['dealer'] <= 0:
        print("You have no money, game over!")
        break
    else:
        if input("Wanna again? y for again,n for quit\n").lower() == "n":
            is_again = True
