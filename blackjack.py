#this is a game of blackjack
import random
import os 



exgame = False
numb = [1,2,3,4,5,6,7,8,9,10,11,12,13]
hand = []
dealer = []

def deal():
    d_card = random.choice(numb) 
    p_card, p_card1 = random.choice(numb), random.choice(numb)
    print("Dealer's showing", d_card)
    print("Player's showing", p_card, "and", p_card1, "\n")
    dealer.append(d_card)
    hand.append(p_card)
    hand.append(p_card1)

def clear():
	if os.name == 'nt':
		os.system('CLS')
	if os.name == 'posix':
		os.system('clear')

def dealer_hit():
    while points_dealer() < 20: 
        card = random.choice(numb)
        points_dealer()
        if card == 11: card = "J"
        elif card == 12: card = "Q"
        elif card == 13: card = "K"
        elif card == 1: card = "A"
        dealer.append(card)

def hit_card():
    card = random.choice(numb)
    if card == 11: card = "J"
    elif card == 12: card = "Q"
    elif card == 13: card = "K"
    elif card == 1: card = "A"
    print("\nYour next card is:", card)
    hand.append(card)

def points_player():
    total = 0
    for card in hand:
        if card == "J" or card == "K" or card == "Q": total += 10
        elif card == "A" and total <= 10: total += 11
        elif card == "A" and total > 10: total += 1
        else: total += card
    return total

def points_dealer():
    total = 0
    for card in dealer:
        if card == "J" or card == "K" or card == "Q": total += 10
        elif card == "A" and total <= 10: total += 11
        elif card == "A" and total > 10: total += 1
        else: total += card
    return total

def results():
    if points_dealer() > 21:
        print("You win! The dealer went over the limit.")
        return 1
      
    elif points_player() > 21: 
        print("You lose. Your points went over 21.")
        return 1
    else:
        return None
    

clear()
print("\nWelcome to BlackJack!\n")
deal()

while exgame == False:

    next_move = input("[H]it, [S]tand or [Q]uit? ")

    if next_move == "H" or next_move == "h":

        hit_card()
        points_player()
        print("\nYour current hand is", hand, ", with a total of", points_player(), "points.\n")
        if results() == None:
            exgame = False
        else:
            results()
            exgame = True

    elif next_move == "S" or next_move == "s":

        dealer_hit()
        print("You got", points_player(), "points.")
        print("The dealer got", points_dealer(), "points.\n")
        results()
        if results == None and points_player() > points_dealer():
            print("Congrats! You win!\n")
        elif results == None and points_dealer() > points_player():
            print("I'm sorry, you lost.\n")
        else: 
            print("It's a tie!\n")
        exgame = True
                
    elif next_move == "Q" or next_move == "q":

        print("\nThank you for playing with us! See you next time.\n")
        exgame = True

    else:    

        print("\nInvalid command, try again.\n")
        exgame = False

    

