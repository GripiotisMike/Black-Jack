import random

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
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
cards = cards * 4

def pc_ende(x):
    pc_sum = sum(x)
    while pc_sum < 17:
        x.append(random.choice(cards))
        pc_sum = sum(x)
    return x


def ace(hand):
    for i in range(len(hand)):
        if hand[i] == 11:
            hand[i] = 1
    return hand


def black_jack():
    print("\n" * 100)
    print(logo)
    play_hand = []
    pc_hand = []
    play_hand.append(random.choice(cards))
    play_hand.append(random.choice(cards))
    pc_hand.append(random.choice(cards))
    pc_hand.append(random.choice(cards))
    print(f"\tYour cards: {play_hand}, current score: {sum(play_hand)}")
    print(f"\tComputer's first card: {pc_hand[0]}")
    if sum(play_hand) == 21:
        print(f"\tYour final hand: {play_hand}, final score: {sum(play_hand)}")
        print(f"\tComputer's final hand: {pc_hand}, final score: {sum(pc_hand)}")
        print("You win! 😄")
    else:
        f = True
        while f:
            k = input("Type 'y' to get another card, type 'n' to pass: ")
            if k == "y":
                play_hand.append(random.choice(cards))
                if sum(play_hand) == 21:
                    print(f"\tYour final hand: {play_hand}, final score: {sum(play_hand)}")
                    pc_hand = pc_ende(pc_hand)
                    print(f"\tComputer's final hand: {pc_hand}, final score: {sum(pc_hand)}")
                    print("You win! 😄")
                    f = False
                    continue
                elif sum(play_hand) > 21:
                    play_hand = ace(play_hand)
                    if sum(play_hand) > 21:
                        print(f"\tYour final hand: {play_hand}, final score: {sum(play_hand)}")
                        pc_hand = pc_ende(pc_hand)
                        print(f"\tComputer's final hand: {pc_hand}, final score: {sum(pc_hand)}")
                        print("You loose! 😭")
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
                pc_hand = pc_ende(pc_hand)
                print(f"\tYour final hand: {play_hand}, final score: {sum(play_hand)}")
                print(f"\tComputer's final hand: {pc_hand}, final score: {sum(pc_hand)}")
                if sum(pc_hand) > sum(play_hand) and sum(pc_hand) <= 21:
                    print("You loose! 😭")
                    f = False
                elif sum(pc_hand) < sum(play_hand):
                    print("You win! 😄")
                    f = False
                elif sum(pc_hand) == sum(play_hand):
                    print("Its a tie! 🤔")
                    f = False
                else:
                    print("You win! 😄")
                    f = False
    k = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if k == "y":
        black_jack()


a = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
while a == "y":
    black_jack()
    a = input("Continue paying? Type 'y' or 'n': ")
