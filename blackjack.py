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
    # This block should be a function
    if d_card == 11: d_card = "J"
    elif d_card == 12: d_card = "Q"
    elif d_card == 13: d_card = "K"
    elif d_card == 1: d_card = "A"
    # Block ends here
    if p_card == 11: p_card = "J"
    elif p_card == 12: p_card = "Q"
    elif p_card == 13: p_card = "K"
    elif p_card == 1: p_card = "A"
    if p_card1 == 11: p_card1 = "J"
    elif p_card1 == 12: p_card1 = "Q"
    elif p_card1 == 13: p_card1= "K"
    elif p_card1 == 1: p_card1 = "A"
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
    while points_dealer() < 17: 
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
    if points_dealer() > 21 :
        print("You win! The dealer went over the limit.\nThank you for playing with us! See you next time.\n")
        return 1
      
    elif points_player() > 21 : 
        print("You lose. Your points went over 21.\nThank you for playing with us! See you next time.\n")
        return 1
    else:
        return 0

    

clear()
print("\nWelcome to BlackJack!\n")
deal()

while exgame == False:

    next_move = input("[H]it, [S]tand or [Q]uit? ")

    if next_move == "H" or next_move == "h":

        hit_card()
        points_player()
        print("\nYour current hand is", hand, ", with a total of", points_player(), "points.\n")
        
        if results() != 0:
            exgame = True
            break

    elif next_move == "S" or next_move == "s":
        dealer_hit()

        print("You got", points_player(), "points.")
        print("The dealer got", points_dealer(), "points.\n")
        
        results()
        
        if results() == 0 and points_player() > points_dealer():
            print("Congrats! You win!\nThank you for playing with us! See you next time.\n")
            break

        elif results() == 0 and points_dealer() > points_player():
            print("I'm sorry, you lost.\nThank you for playing with us! See you next time.\n")
            break

        elif results() == 0 and points_dealer() == points_player():
            print("It's a tie!\nThank you for playing with us! See you next time.\n")
            break


        exgame = True
                
    elif next_move == "Q" or next_move == "q":
        print("\nThank you for playing with us! See you next time.\n")
        exgame = True

    else:    
        print("\nInvalid command, try again.\n")
        exgame = False
