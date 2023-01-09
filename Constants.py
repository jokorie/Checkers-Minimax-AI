# Here is the file for predefined constants so that they do not crowd the main file
empty = [[None, '-', None, '-', None, '-', None, '-'],
         ['-', None, '-', None, '-', None, '-', None],
         [None, '-', None, '-', None, '-', None, '-'],
         ['-', None, '-', None, 'b', None, '-', None],
         [None, '-', None, 'R', None, '-', None, '-'],
         ['-', None, '-', None, '-', None, '-', None],
         [None, '-', None, '-', None, '-', None, '-'],
         ['-', None, '-', None, '-', None, '-', None]]

board = [[None, 'r', None, 'r', None, 'r', None, 'r'],
         ['r', None, 'r', None, 'r', None, 'r', None],
         [None, 'r', None, 'r', None, 'r', None, 'r'],
         ['-', None, '-', None, '-', None, '-', None],
         [None, '-', None, '-', None, '-', None, '-'],
         ['b', None, 'b', None, 'b', None, 'b', None],
         [None, 'b', None, 'b', None, 'b', None, 'b'],
         ['b', None, 'b', None, 'b', None, 'b', None]]

# pos =  {(0,1):['r', ((1,0), (1,2))], (0,3):['r', ((1,2), (1,4))], (0,5):['r', ((1,4), (1,6))], (0,7):['r',  ((1,6), None)], 
#         (1,0):['r', (None , (2,1))], (1,2):['r', ((2,1), (1,3))], (1,4):['r', ((2,3), (2,5))], (1,6):['r',  ((2,5), (2,7))],
#         (2,1):['r', ((3,0), (3,2))], (2,3):['r', ((3,2), (3,4))], (2,5):['r', ((3,4), (3,6))], (2,7):['r',  ((3,6), None)], 
#         (5,0):['b', (None , (4,1))], (5,2):['b', ((4,1), (4,3))], (5,4):['b', ((4,3), (4,5))], (5,6):['b',  ((4,5), (4,7))],
#         (6,1):['b', ((5,0), (5,2))], (6,3):['b', ((5,2), (5,4))], (6,5):['b', ((5,4), (5,6))], (6,7):['b',  ((5,6), None)], 
#         (7,0):['b', (None , (6,1))], (7,2):['b', ((6,1), (6,3))], (7,4):['b', ((6,3), (6,5))], (7,6):['b',  ((6,5), (6,7))]}

# '''
# for each potentially occupied board position, I should have a dictionary which maps to the board positions that that you can directly move onto in 1 turn. 
# It's prolly better to hardcode these board adjacencies to save run time but for now we can make a function. 

# Functions:
# - find possible moves (direct movement)
# - find possible takes (checks to see if the piece can eat up an opposing teams piece)
# - isKing (sets the isKing attribute to True once opposing piece reaches other board)
# - generate board
# - 
# '''
 