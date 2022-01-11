#Step 1)Import library provided 'connectfour.py'

import connectfour as func

#Step 2)Let's define the parameters of the problem by getting the players decision for how many rows and columns

def how_many_rows_columns() -> (int,int):

    rows = input('How many rows?')

   # print(rows.isdigit())
    #print((func.MIN_ROWS <= int(rows) <= func.MAX_ROWS))
    
    while not ((rows.isdigit()) and (func.MIN_ROWS <= int(rows) <= func.MAX_ROWS)):

        rows = input('How many rows?')

    columns = input('How many columns?')
        
    while not  ((columns.isdigit()) and (func.MIN_COLUMNS <= int(columns) <= func.MAX_COLUMNS)):

          columns = input('How many columns?')
            
    return int(columns),int(rows)

#Step 3)Lets display the board

#Double check module requirements, make sure you have 5 modules shell, network, sockets, his library, yours

#Step 3)Yellow or Red? Referencing the YELLOW and RED Global variables equal 

def yellow_or_red(b: int) -> str:
    '''
    Returns 'R' or
    Returns 'Y' or
    Returns '.' the empty space
    '''
    if b == func.YELLOW:
        return 'Y'
    elif b == func.RED:
        return 'R'
    else:
        return '.'

#Step 4)This is where a decision is made of what column to drop or pop a players puck
def get_move(columns) -> (int,str):
    '''
    This is where the player chooses a column which returns the int of the tuple
    Then the player choses if they want to "Drop" or "Pop"
    '''
    while True:
        
        column = input('What column would you like to drop or pop?')

        if not column.isdigit():
            continue
        column = int(column)

        if not (0 < column <= columns):
            continue
        break
        
    while True:

        drop_or_pop = input("Would you like to 'Drop' or 'Pop'? Enter one of the two options.")

        if drop_or_pop.lower()!='drop' and drop_or_pop.lower()!='pop':
            continue
        break
        
    return((column,drop_or_pop))


#Step 5)Display the board, takes in the GameState
    
def display_game_board(current_board: func.GameState, rows: int, columns: int) -> None:
    for column_index in range(1,columns+1):
        if column_index >= 9:
            print(str(column_index) + ' ', end ='')
        else:
            print(str(column_index) + '  ', end ='')
    print('')

    for row_index in range(rows): 
        for column_index in range(columns): 
            if column_index == 0:
                print(yellow_or_red(current_board.board[column_index][row_index]) + '  ', end = '')
            else:
                print( yellow_or_red(current_board.board[column_index][row_index]) + '  ', end = '')
        print('')


#Step 6)Function accepts Gamestate, column, and move from get_move()function and make changes to the game state
    
def player_move(current_board: func.GameState, column : int, move : str) -> func.GameState:

    #if the player chooses to drop down a peice we utilize the drop() funciton from the library, we pass in the current_board and the column we want to drop a peice into
    if move.lower()== 'drop':
        return func.drop(current_board, column - 1)

    elif move.lower() == 'pop':
        return func.pop(current_board, column -1)

    else:
        raise func.InvalidMoveError()

#Step 7)For this step we utilize the red_or_yellow function to turn and int into a string
#       This way we can print the turn 
    
def red_or_yellow(var: int) -> str:
    '''
    Returns a string determining if the player wants to start first with Red
    Or start second with a yellow puck
    The only inputs accepted are 0,1,2
    '''
    if var == func.YELLOW:
        return "Yellow"
    elif var == func.RED:
        return "Red"
    else:
        return "None"

#we take in the GameState and now we can print using the red_or_yellow function 
def turn(current_board = func.GameState):
    '''
    Print's the turn of the player by referencing the red_or_yellow function and passing in an int from the namedtuple element 'turn'
    '''
    print(f'Turn of the {red_or_yellow(current_board.turn)} player.')
