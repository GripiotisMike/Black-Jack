import random

# ASCII art for Blackjack game logo
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

# List of card values
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
cards = cards * 4  # Duplicate the deck for multiple games

# Function for computer's turn, where it draws cards until its total is 17 or more
def pc_ende(x):
    pc_sum = sum(x)
    while pc_sum < 17:  # Computer stops drawing cards if total is 17 or higher
        x.append(random.choice(cards))
        pc_sum = sum(x)
    return x

# Function to adjust ace values from 11 to 1 if the hand exceeds 21
def ace(hand):
    for i in range(len(hand)):
        if hand[i] == 11:
            hand[i] = 1
    return hand

# Main game logic for Blackjack
def black_jack():
    print("\n" * 100)  # Clear the screen
    print(logo)
    
    # Initialize player and computer hands
    play_hand = [random.choice(cards), random.choice(cards)]
    pc_hand = [random.choice(cards), random.choice(cards)]
    
    # Display initial hands
    print(f"\tYour cards: {play_hand}, current score: {sum(play_hand)}")
    print(f"\tComputer's first card: {pc_hand[0]}")
    
    # If the player has a Blackjack (21) initially, they win
    if sum(play_hand) == 21:
        print(f"\tYour final hand: {play_hand}, final score: {sum(play_hand)}")
        print(f"\tComputer's final hand: {pc_hand}, final score: {sum(pc_hand)}")
        print("You win! 😄")
    else:
        # Game loop where the player decides to hit or stand
        f = True
        while f:
            k = input("Type 'y' to get another card, type 'n' to pass: ")
            if k == "y":
                play_hand.append(random.choice(cards))
                
                # Check for Blackjack or bust
                if sum(play_hand) == 21:
                    print(f"\tYour final hand: {play_hand}, final score: {sum(play_hand)}")
                    pc_hand = pc_ende(pc_hand)
                    print(f"\tComputer's final hand: {pc_hand}, final score: {sum(pc_hand)}")
                    print("You win! 😄")
                    f = False
                    continue
                elif sum(play_hand) > 21:
                    play_hand = ace(play_hand)  # Adjust for ace if bust
                    if sum(play_hand) > 21:
                        print(f"\tYour final hand: {play_hand}, final score: {sum(play_hand)}")
                        pc_hand = pc_ende(pc_hand)
                        print(f"\tComputer's final hand: {pc_hand}, final score: {sum(pc_hand)}")
                        print("You lose! 😭")
                        f = False
                    else:
                        print(f"Your cards: {play_hand}, current score: {sum(play_hand)}")
                        print(f"Computer's first card: {pc_hand[0]}")
                        continue
                else:
                    print(f"Your cards: {play_hand}, current score: {sum(play_hand)}")
                    print(f"Computer's first card: {pc_hand[0]}")
                    continue
            else:
                # Computer's turn
                pc_hand = pc_ende(pc_hand)
                print(f"\tYour final hand: {play_hand}, final score: {sum(play_hand)}")
                print(f"\tComputer's final hand: {pc_hand}, final score: {sum(pc_hand)}")
                
                # Determine winner
                if sum(pc_hand) > sum(play_hand) and sum(pc_hand) <= 21:
                    print("You lose! 😭")
                    f = False
                elif sum(pc_hand) < sum(play_hand):
                    print("You win! 😄")
                    f = False
                elif sum(pc_hand) == sum(play_hand):
                    print("It's a tie! 🤔")
                    f = False
                else:
                    print("You win! 😄")
                    f = False

    # Ask if the player wants to play again
    k = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if k == "y":
        black_jack()  # Restart the game

# Initial prompt to start the game
a = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
while a == "y":
    black_jack()
    a = input("Continue playing? Type 'y' or 'n': ")
