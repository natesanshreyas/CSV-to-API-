def display_game(game_list):
    print(game_list[0:3])
    print(game_list[3:6])
    print(game_list[6:9])
    print(game_list)

def user_choice():
    
    choice = 'wrong'
        
    while True:
        choice = input("Please enter in a number: ")
        
        if choice not in ['0','1','2','3','4','5','6','7','8']:
            print("Not an applicable choice, try again!")
            continue
            
        elif choice.isdigit() == False:
            print ("Try again!")
            continue
            
        else:
            print(f'You chose {choice}')
            break
        
    
    return int(choice)

def replacement_choice(game_list, position):
        
    user_placement = 'none'
    
    while True:
        user_placement = input("Place either X or O at the selected position")


        if user_placement not in ["X","O"]: 
            print("Not an applicable choice, try again!")
            
        else:
            print ("Next player's move!")
            break

    game_list[position] = user_placement
    
    return game_list

def position_choice():
    
    # This original choice value can be anything that isn't an integer
    choice = 'wrong'
    
    # While the choice is not a digit, keep asking for input.
    while choice not in ['0','1','2','3','4','5','6','7','8']:
        
        # we shouldn't convert here, otherwise we get an error on a wrong input
        choice = input("Pick a position to replace between 0 and 8: ")
        
        if choice not in ['0','1','2','3','4','5','6','7','8']:
            # THIS CLEARS THE CURRENT OUTPUT BELOW THE CELL
            clear_output()
            
            print("Sorry, but you did not choose a valid position (0,1,2)")
            
    
    # Optionally you can clear everything after running the function
    # clear_output()
    
    # We can convert once the while loop above has confirmed we have a digit.
    return int(choice)

def gameon_choice():
    
    # This original choice value can be anything that isn't a Y or N
    choice = 'wrong'
    
    # While the choice is not a digit, keep asking for input.
    while choice not in ['Y','N']:
        
        # we shouldn't convert here, otherwise we get an error on a wrong input
        choice = input("Would you like to keep playing? Y or N ")

        
        if choice not in ['Y','N']:
            # THIS CLEARS THE CURRENT OUTPUT BELOW THE CELL
            clear_output()
            
            print("Sorry, I didn't understand. Please make sure to choose Y or N.")
            
    
    # Optionally you can clear everything after running the function
    # clear_output()
    
    if choice == "Y":
        # Game is still on
        return True
    else:
        # Game is over
        print ("No worries! Have a great day.")
        return False


def x_win(game_list):
    choice1 = "X"
    
    if (game_list[0] == game_list[1] == game_list[2] == choice1 and game_list[0] != "") or \
       (game_list[0] == game_list[3] == game_list[6] == choice1 and game_list[0] != "") or \
       (game_list[1] == game_list[4] == game_list[7] == choice1 and game_list[1] != "") or \
       (game_list[2] == game_list[5] == game_list[8] == choice1 and game_list[2] != "") or \
       (game_list[0] == game_list[4] == game_list[8] == choice1 and game_list[0] != "") or \
       (game_list[2] == game_list[4] == game_list[6] == choice1 and game_list[2] != ""):
        print ("Congrats! Player X won the game")
        return True
    return False



def y_win(game_list):
    choice2 = "O"
    
    if (game_list[0] == game_list[1] == game_list[2] == choice2 and game_list[0] != "") or \
       (game_list[0] == game_list[3] == game_list[6] == choice2 and game_list[0] != "") or \
       (game_list[1] == game_list[4] == game_list[7] == choice2 and game_list[1] != "") or \
       (game_list[2] == game_list[5] == game_list[8] == choice2 and game_list[2] != "") or \
       (game_list[0] == game_list[4] == game_list[8] == choice2 and game_list[0] != "") or \
       (game_list[2] == game_list[4] == game_list[6] == choice2 and game_list[2] != ""):
        print ("Congrats! Player O won the game")
        return True
    return False


def game_loop(game_list):
    if x_win(game_list):
        print ("Congrats! Player X won the game")
        return False  # End the game
    
    elif y_win(game_list):
        print ("Congrats! Player O won the game")
        return False  # End the game
    
    # If no one has won and there are no more empty spaces, it's a draw
    elif '' not in game_list:
        print("The game is a draw!")
        return False  # End the game

    else:
        return True  # Continue the game


from IPython.display import clear_output

game_on = True

# First Game List
game_list = ['','','',
             '','','',
             '','','',]



while game_on:
    # Clear any historical output and show the game list
    clear_output()
    display_game(game_list)
    
    # Have player choose position
    position = position_choice()
    
    # Rewrite that position and update game_list
    game_list = replacement_choice(game_list,position)
    
    # Clear Screen and show the updated game list
    clear_output()
    display_game(game_list)

    # Check if the game continues
    game_on = game_loop(game_list)
    
    # If the game is still on, ask if you want to keep playing
    if game_on:
        game_on = gameon_choice()
