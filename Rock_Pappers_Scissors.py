'''This is a simple program to play rock, pappers and scissors with the computer. It has a scoring system and checks if you want to play again.
This program does not check for invalid inputs, it could be implemented by a try, except function.
'''


import random #Random.choice function is required to randomise the computers choice. 

player_score, computer_score = 0 , 0 #Initialize variabels 
#Function to play the game
def play(): 
    global player_score
    global computer_score#Initialize variabels, make them global so we can access them later on. 
    player = input("'r' for rock, 'p' for paper, 's' for scissors. > ") #Get the users choice
    computer = random.choice(['r','s','p',]) #Computer chooses randomly between rock,papers and scissors.

    if player == computer: #If tie
        return "The computer chose " + computer + ". You tied! Press K to play again or Q to quit "
    
    if is_win(player,computer): #If player wins
        player_score += 1 
        return "The computer chose " + computer + ". You won! Press K to play again or Q to quit"
#If no tie or win --> player lost. 
    computer_score += 1
    return "The computer chose " + computer + ". You lost! Press K to play again or Q to quit"
    

#Function to check if the player won, all the different cases
def is_win(player,computer):
    WINNING_MOVES = { #Winning cases for the player, match it with the computers choice. 
    'r': 's',
    'p': 'r',
    's': 'p'
}
    return WINNING_MOVES.get(player) == computer


while True:
    print(play())
    play_again = input()
    if play_again == 'K' or play_again == 'k':
        continue #Restarts the game
    elif play_again == 'Q' or play_again == 'q':
        print(f"You scored {player_score}. The computer scored {computer_score}.")
        break