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
    r_pieces = board.count('r')
    b_pieces = board.count('b')
    if r_pieces == 0:
        print('game over, b team wins')
        return -1000
    elif b_pieces == 0:
        print('game over, b team wins')
        return 1000
    else:
        return ((12-b_pieces)**2 - (12-r_pieces)**2)
