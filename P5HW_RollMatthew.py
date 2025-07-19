import random
import time

# Matthew Roll
# July 10, 2025
# P5HW
# This program creates a card game where players guess if their card is higher or lower than the computer's card to reach 50 points first, with suit rankings and unique cards

def create_card():
    suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
    ranks = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    suit_values = {'Spades': 4, 'Hearts': 3, 'Diamonds': 2, 'Clubs': 1}
    while True:
        suit = random.choice(suits)
        rank = random.choice(list(ranks.keys()))
        return {'suit': suit, 'rank': rank, 'value': ranks[rank], 'suit_value': suit_values[suit]}
#Prompt: "Change the scoring scale to 5 points for successful guess, and apply a rank order for scoring to the suites of the cards similar to Texas Holdem. Also do not allow for both players to have the same card type and suite."
#Response Summary: Updated scoring to 5 points, added suit rankings (Spades > Hearts > Diamonds > Clubs), and ensured unique cards.

def determine_winner(player_score, computer_score):
    if player_score >= 50:
        return "Player"
    elif computer_score >= 50:
        return "Computer"
    return None

def play_round(player_card, computer_card):
    while player_card['suit'] == computer_card['suit'] and player_card['rank'] == computer_card['rank']:
        computer_card = create_card()
    print(f"Your card: {player_card['rank']} of {player_card['suit']}")
    guess = input("Is the computer's card higher or lower? (h/l): ").lower()
#Prompt: "The code is not taking into account if I'm guessing that my card is lower than the computer's, and giving me the proper points for guessing correctly."
#Response Summary: Fixed the play_round function logic to correctly handle lower guesses.
    if guess not in ['h', 'l']:
        print("ah ah ah you didnt say the magic letter")
        return 0
    
    print(f"Computer's card: {computer_card['rank']} of {computer_card['suit']}")
    time.sleep(1)
    
    # Compare both rank and suit values
    if (guess == 'h' and (computer_card['value'] > player_card['value'] or 
                          (computer_card['value'] == player_card['value'] and computer_card['suit_value'] > player_card['suit_value']))) or \
       (guess == 'l' and (computer_card['value'] < player_card['value'] or 
                          (computer_card['value'] == player_card['value'] and computer_card['suit_value'] < player_card['suit_value']))):
        print("😊")
        return 5
    else:
        print("😢")
        return 0

def main():
    player_score = 0
    computer_score = 0
    winner = None
    
    while winner is None:
        player_card = create_card()
        computer_card = create_card()
#Prompt: "This game didn't end in a draw from my last test the human player was winning. Please remove the round limit in the code. Also ensure that the game continues until there is a clear winner."
#Response Summary: Removed round limit, used while True until a winner.
        points = play_round(player_card, computer_card)
        if points > 0:
            player_score += points
        else:
            computer_score += 5  # Computer gets 5 points for player's wrong guess
        
        print(f"Player Score: {player_score}, Computer Score: {computer_score}")
        
        winner = determine_winner(player_score, computer_score)
        if winner:
            print("👍")
            print(f"{winner} wins!")

if __name__ == "__main__":
    main()