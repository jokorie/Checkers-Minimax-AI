import copy

empty = [[None, '-', None, '-', None, '-', None, '-'],
         ['-', None, '-', None, '-', None, '-', None],
         [None, '-', None, '-', None, '-', None, '-'],
         ['-', None, '-', None, '-', None, '-', None],
         [None, '-', None, '-', None, '-', None, '-'],
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

pos =  {(0,1):['r', ((1,0), (1,2))], (0,3):['r', ((1,2), (1,4))], (0,5):['r', ((1,4), (1,6))], (0,7):['r',  ((1,6), None)], 
        (1,0):['r', (None , (2,1))], (1,2):['r', ((2,1), (1,3))], (1,4):['r', ((2,3), (2,5))], (1,6):['r',  ((2,5), (2,7))],
        (2,1):['r', ((3,0), (3,2))], (2,3):['r', ((3,2), (3,4))], (2,5):['r', ((3,4), (3,6))], (2,7):['r',  ((3,6), None)], 
        (5,0):['b', (None , (4,1))], (5,2):['b', ((4,1), (4,3))], (5,4):['b', ((4,3), (4,5))], (5,6):['b',  ((4,5), (4,7))],
        (6,1):['b', ((5,0), (5,2))], (6,3):['b', ((5,2), (5,4))], (6,5):['b', ((5,4), (5,6))], (6,7):['b',  ((5,6), None)], 
        (7,0):['b', (None , (6,1))], (7,2):['b', ((6,1), (6,3))], (7,4):['b', ((6,3), (6,5))], (7,6):['b',  ((6,5), (6,7))]}

'''
for each potentially occupied board position, I should have a dictionary which maps to the board positions that that you can directly move onto in 1 turn. 
It's prolly better to hardcode these board adjacencies to save run time but for now we can make a function. 

Functions:
- find possible moves (direct movement)
- find possible takes (checks to see if the piece can eat up an opposing teams piece)
- isKing (sets the isKing attribute to True once opposing piece reaches other board)
- generate board
- 
'''
 
class TreeNode():
    def __init__(self, pos, parent = None, depth = 0, children = []):
        self.parent = parent
        self.value = None
        self.depth = depth
        self.children = children
        self.maxTurn = (depth%2 == 0)
        self.trail = False
        self.pos = pos
        self.board = empty
        #dictionary = {(current space):[occuppying piece, (accessible space, accessible space)]}
    
    #HELPER FUNCTIONS
    def get_pos(self):
        return copy.deepcopy(self.pos)

    def set_children(self, childlist):
        if len(self.get_children()) == 0:
            self.children = childlist[:]
        else:
            self.children += childlist

    def make_child(self, pos, piece, dir_index):
        new_pos = self.get_pos()
        new_pos[self.pos[key][1][dir_index]][0] = piece
        new_pos[key][0] = '-'
        child = TreeNode(new_pos, self, self.depth + 1)
        self.set_children([child])
        return child
    
    def set_parent(self, parent):
        self.parent = parent

    def set_board(self, board):
        self.board = board

    def make_board(self, board = empty):
        for key in self.pos:
            piece = self.pos[key][0]
            board[key[0]][key[1]] = piece
        self.set_board(board)    
        
    def display_board(self):
        print('-------Printing Board-------')
        for row in self.board:
            print(row)
        print('-----Finished Printing-----')

    # def calc_adj_pos(self, team, pos):
    #     if team == 'r':
    #         delta_y = 1
    #     newpos0 = (pos[0]+delta_y, pos[0]-1)
    #     if pos[0]+delta_y, pos[0]-1
    #     newpos1 = (pos[0]+delta_y, pos[0]+1)
        
    #     if 
    #     return ((pos[0]+delta_y, pos[0]-1),(pos[0]+delta_y, pos[0]+1))
        

            adj_pos = 
    #END OF HELPER FUNCTIONS
    
    def check_open_pos(self):
        for key in self.pos:
            for i in range(2):
                #instantiates current piece
                piece = self.pos[key][0]
                #checks to to see that either left of right adjacent piece exist. Mainly for literal edge case
                if self.pos[key][1][i] == None:
                    continue
                #instantiates adjacent piece
                targ_piece = self.pos[self.pos[key][1][i]][0]
                assert piece == 'b' or piece == 'r' or piece == '-'
                if targ_piece == piece:                
                    continue
                elif targ_piece == '-':
                    child = self.make_child(self.pos, piece, i)
                    self.set_children[child]
                else:
                    #when the adjacent piece is of the opposite team run the can jump method
                    #returns (Bool representing if its possible to jump in this scenario, Treenode object)
                    temp = self.can_jump(key, i, targ_piece)
                    if temp[0] == True:
                        #unsure if necesary
                        temp[1].set_parent(self)
                        self.set_children[temp[1]]
                    
    def can_jump(self, key, dir_index, jumped_piece):
        piece = self.pos[key][0]
        if piece == 'r':
            opp_piece = 'b'
        elif piece == 'b':
            opp_piece = 'r'

        if (jumped_piece == opp_piece) and self.pos[self.pos[self.pos[key][1][dir_index]][1][dir_index]][0] == '-':
            #store as child node
            #make can jump more function
            new_pos = self.get_pos(self.pos)
            new_pos[self.pos[key][1][dir_index]][0] = piece
            new_pos[key][0] = '-'
            child = TreeNode(new_pos, self, self.depth + 1)
            # child.can_jump(key, 'RIGHT', right_piece)
            return (True, child)
        return False
    
if __name__ == '__main__':
    root = TreeNode(pos)
    root.make_board()
    root.display_board()
    root.check_open_pos()
    print(len(root.children))
