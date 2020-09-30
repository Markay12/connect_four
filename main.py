#Name: Mark Ashinhust
#Date: 09/29/2020
#Description: Game of connect four with the command line. Play against yourself or a friend and see who can get four in a row first!


# import numpy package as interpreter for arrays
import numpy as nump

def game_board():
    game_board = nump.zeros((6, 7)) #create a game board that is an array of 6 rows and 7 columns
    return game_board

def is_placement_valid(game, column): #check to make sure the placement of the game pieces are valid
    #index starts at 0, make sure the top column is filled row 5 (top) and selected column
    #board[row][column]
    return game[5][column] == 0 #boolean statement to check if placement is valid

def is_player_selection(player_selection): #check player selection 
    if player_selection >= 1 or player_selection <= 7:
        return True
    else:
        return False

def get_next(game, column):
    for rows in range(6):
        if game[rows][column] == 0: #if this column and row has a zero, nothing has been placed == VALID LOCATION
            return rows #where can we now place this row

def place(game, row, column, player_piece):
    game[row][column] = player_piece #place the players piece at this specified and checked location

def player_win(game, player_piece): #to check winning conditions
    #check horizontal win
    for column in range(4): #has to have 4 in a row to win, so we check 4 times and 4 columns
        for row in range(6): #check all of the rows
            #go through each column in a line and see if this player piece appears in each, same row next column over
            if game[row][column] == player_piece:
                if game[row][column+1] == player_piece:
                    if game[row][column+2] == player_piece:
                        if game[row][column+3] == player_piece:
                            return True #if all of these return True we want to return True back to the user

    #check for a vertical win
    #same idea as the horizontal check, however, now we just increment the rows
    for column in range(7): #total columns
        for row in range(3): #move through rows checking for a 4 in a row vertically
            if game[row][column] == player_piece:
                if game[row+1][column] == player_piece:
                    if game[row+2][column] == player_piece:
                        if game[row+3][column] == player_piece:
                            return True #return true if we have a four in a row vertically

    for column in range(4): #check four columns
        for row in range(3): #increment the rows stepwise to complete the positive slope upwards
            if game[row][column] == player_piece:
                if game[row+1][column+1] == player_piece:
                    if game[row+2][column+2] == player_piece:
                        if game[row+3][column+3] == player_piece:
                            return True #return true for positive slope

    for column in range(4): #check four columns
        for row in range(3, 6): #we only want to check from the top down because of the negative slopes
            if game[row][column] == player_piece:
                if game[row-1][column+1] == player_piece:
                    if game[row-2][column+2] == player_piece:
                        if game[row-3][column+3] == player_piece:
                            return True #return true for negative slope

    return False #return false if none of our cases come back as true

game = game_board() #draws the initial gameboard
game_over = False #create game_over variable for main game loop
turn = 0 #initialize turn to 0 which will start with player one
winner = 0 #winner set to 1 if player one wins and 2 if player 2 wins

while not game_over:

    #init check while going through loop to see if someone has won
    if player_win(game, 1): #check to see if player one has won
        winner = 1 #set var to 1 so we know player one won
        game_over = True #endgame
    elif player_win(game, 2): #check to see if player two has won
        winner = 2 #set var to 2 so we know player one won
        game_over = True #endgame

    elif turn % 2 == 0: #if turn is an even number it is player one turn

        print("Player 1 Turn\n---------------")
        player_1_selection = int(input("Choose a column --> ")) #cast input to integer for column selection
        print("\n") #spacing for game board

        player_1_selection = player_1_selection - 1 #columns begin at 1 for user readability

        if is_player_selection(player_1_selection) and is_placement_valid(game, player_1_selection): #if the player input is out of range, game will not play and turn will not increment, gives error message

            

            #placement of the piece
            chosen_row = get_next(game, player_1_selection) #get the next row that is open for placement
            place(game, chosen_row, player_1_selection, 1) #choose game, row specified, player column specified, and place a 1 for player 1

            #nump.flip(<matrix>, <axis>) ; in this case we flipped over the x-axis
            print(nump.flip(game, 0)) # flip the game board to show correct output
            print("\n") #spacing
            turn = turn + 1 #player has played, turn gets incremented


        else: #if player is within game bounds
            print("Input out of range\n---Try Again---\n")


    elif turn % 2 != 0: #if turn is an odd number it is player two turn
        print("Player 2 Turn\n------------")
        player_2_selection = int(input("Choose a column --> "))
        print("\n") #spacing for game board

        player_2_selection = player_2_selection - 1 #columns begin at 1

        if is_player_selection(player_2_selection) and is_placement_valid(game, player_2_selection): #if the player input is out of range, game will not play and turn will not increment, gives error message
            
            #placement of the game piece
            chosen_row = get_next(game, player_2_selection)
            place(game, chosen_row, player_2_selection, 2) #choose the correct game board, the next open row, player column selection and a 2 for player 2

            print(nump.flip(game, 0)) #print the game updated, flip the board as we initially show it starting top down 
            print("\n")

            turn = turn + 1 #increment the turns

        else: #if the player makes a correct selection
            print("Input out of range\n---Try Again---\n")

    
if winner == 1: #final game win, check variable winner to see which player one and respective message
    print("---------------------\n/////////////////////\n\nGame Over\n\nPlayer 1 Wins\n\n/////////////////////\n---------------------")
if winner == 2:
   print("---------------------\n/////////////////////\n\nGame Over\n\nPlayer 2 Wins\n\n/////////////////////\n---------------------") 
               




