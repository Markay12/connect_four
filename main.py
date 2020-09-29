# import numpy package as interpreter for arrays
import numpy as nump

def game_board():
    game_board = nump.zeros((6, 7)) #create a game board that is an array of 6 rows and 7 columns
    return game_board

def is_placement_valid(game, column): #check to make sure the placement of the game pieces are valid
    #index starts at 0, make sure the top column is filled row 5 (top) and selected column
    #board[row][column]
    return game[5][column] == 0 #boolean statement to check if placement is valid

def 




game = game_board() #draws the initial gameboard
game_over = False #create game_over variable for main game loop
turn = 0 #initialize turn to 0 which will start with player one

while not game_over:

    if turn % 2 == 0: #if turn is an even number it is player one turn
        print("Player 1 Turn\n---------------")
        player_1_selection = int(input("Choose a column --> ")) #cast input to integer for column selection
        print("\n") #spacing for game board

        player_1_selection = player_1_selection - 1 #columns begin at 1 for user readability

        if player_1_selection > 7 or player_1_selection < 1: #if the player input is out of range, game will not play and turn will not increment, gives error message
            print("Input out of range\n---Try Again---\n")
        elif player_1_selection > 0 and player_1_selection < 8: #if player is within game bounds

            #TODO: update game here

            #nump.flip(<matrix>, <axis>) ; in this case we flipped over the x-axis
            print(nump.flip(game, 0)) # flip the game board to show correct output
            print("\n") #spacing
            turn = turn + 1 #player has played, turn gets incremented



    if turn % 2 != 0: #if turn is an odd number it is player two turn
        print("Player 2 Turn\n------------")
        player_2_selection = int(input("Choose a column --> "))
        print("\n") #spacing for game board

        player_2_selection = player_2_selection - 1 #columns begin at 1

        if player_2_selection > 7 or player_2_selection < 1: #if the player input is out of range, game will not play and turn will not increment, gives error message
            print("Input out of range\n---Try Again---\n")
        elif player_2_selection > 0 and player_2_selection < 8: #if the player makes a correct selection

            # TODO: Update game here!

            print(nump.flip(game, 0)) #print the game updated, flip the board as we initially show it starting top down 
            print("\n")

            turn = turn + 1 #increment the turns





