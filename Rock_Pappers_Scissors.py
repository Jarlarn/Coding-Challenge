'''This is a simple program to play rock, pappers and scissors with the computer. It has a scoring system and checks if you want to play again.
This program does not check for invalid inputs, it could be implemented by a try, except function.
'''


import random #Random.choice function is required to randomise the computers choice. 

player_score, computer_score = 0 , 0 #Initialize variabels 
#Function to play the game
def play(): 
    global player_score
    global computer_score#Initialize variabels, make them global so we can access them later on. 

    try:
        player = input("'r' for rock, 'p' for paper, 's' for scissors. > ")
        if player not in ('r', 'p', 's'):
            raise ValueError(f"Invalid input: {player}")
    except ValueError as e:
        return str(e)

    computer = random.choice(['r', 'p', 's'])
    
    if player == computer:
        return f"The computer chose {computer}. You tied! Press K to play again or Q to quit."
    
    if is_win(player, computer):
        player_score += 1 
        return f"The computer chose {computer}. You won! Press K to play again or Q to quit."
    
    computer_score += 1
    return f"The computer chose {computer}. You lost! Press K to play again or Q to quit."
    

#Function to check if the player won, all the different cases
def is_win(player,computer):
    WINNING_MOVES = { #Winning cases for the player, match it with the computers choice. 
    'r': 's',
    'p': 'r',
    's': 'p'
}
    return WINNING_MOVES.get(player) == computer

def restart_game():
    while True:
        try:
            play_again = input("Press K to play again or Q to quit > ")
            if play_again not in ('K', 'k', 'Q', 'q'):
                raise ValueError(f"Invalid input: {play_again}")
            break  # Exit the loop if the input is valid
        except ValueError as e:
            print(str(e))
    
    if play_again.lower() == 'k':
        return True  # Restarts the game
    else:
        return False  # Quits the game

#Main functions that runs the entire game
def main():
    while True:
        print(play())
        if not restart_game():
            print(f"You scored {player_score}. The computer scored {computer_score}.")
            break

main()