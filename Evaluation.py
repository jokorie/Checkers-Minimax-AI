#Board Evaluation File
# Board (For Reference):
# board = [[None, 'r', None, 'r', None, 'r', None, 'r'],
#          ['r', None, 'r', None, 'r', None, 'r', None],
#          [None, 'r', None, 'r', None, 'r', None, 'r'],
#          ['-', None, '-', None, '-', None, '-', None],
#          [None, '-', None, '-', None, '-', None, '-'],
#          ['b', None, 'b', None, 'b', None, 'b', None],
#          [None, 'b', None, 'b', None, 'b', None, 'b'],
#          ['b', None, 'b', None, 'b', None, 'b', None]]
# red team is the maximizing player, while black team is the minimizing player

def evaluate(board):
    '''
    input type: list(list)
    return type: integer
    
    Function takes in a 2D nested list representing the current board and 
    returns a value representing which team is winning at the current snapshot
    '''
    r_pieces = 0
    b_pieces = 0
    for row in board:
        r_pieces += row.count('r') + 2*row.count('R')
        b_pieces += row.count('b') + 2*row.count('B')
    if r_pieces == 0:
        print('game over, black team wins')
        return -1000
    elif b_pieces == 0:
        print('game over, red team wins')
        return 1000
    else:
        return ((12-b_pieces)**2 - (12-r_pieces)**2)
