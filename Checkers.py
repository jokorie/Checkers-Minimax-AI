import copy
from Constants import *

class TreeNode():
    def __init__(self, board = empty, parent = None, depth = 0, children = []):
        self.parent = parent
        self.value = None
        self.depth = depth
        self.children = children
        self.maxTurn = (depth%2 == 0)
        self.trail = False
        self.board = board
    
    #HELPER FUNCTIONS
    def get_board(self):
        return copy.deepcopy(self.board)
    
    def get_children(self):
        return self.children[:]

    def set_children(self, childlist):
        if len(self.get_children()) == 0:
            self.children = childlist[:]
        else:
            self.children += childlist

    def make_child(self, curr_pos, pos):
        targ_pos_y = pos[0]
        targ_pos_x = pos[1]
        new_board = self.get_board()
        new_board[targ_pos_y][targ_pos_x] = self.board[curr_pos[0]][curr_pos[1]]
        new_board[curr_pos[0]][curr_pos[1]] = '-'
        child = TreeNode(new_board, self, self.depth + 1)
        self.set_children([child])
        return child
    
    def set_parent(self, parent):
        self.parent = parent

    def set_board(self, board):
        self.board = board   
        
    def display_board(self):
        print('-------Printing Board-------')
        for row in self.board:
            print(row)
        print('-----Finished Printing-----')

    def calc_adj_pos(self, team, pos):
        if team == 'r':
            delta_y = 1
        elif team == 'b':
            delta_y = -1
        newpos0 = [pos[0]+delta_y, pos[1]-1]
        newpos1 = [pos[0]+delta_y, pos[1]+1]
        adj_pos = [newpos0, newpos1]
        for i in range(2):
            for j in range(2):
                if adj_pos[i][j] < 0 or adj_pos[i][j] > 7:
                    adj_pos[i] = None
        return adj_pos

        def empty_pos(self, pos, board):
            board[pos[0]][pos[1]] = '-'
    #END OF HELPER FUNCTIONS

    def can_jump(self, curr_pos, adj_pos, k, jumped_piece):
        #where k is the direction index
        piece = self.board[curr_pos[0]][curr_pos[1]]
        if piece == 'r':
            opp_piece = 'b'
        elif piece == 'b':
            opp_piece = 'r'
        new_adj_pos = self.calc_adj_pos(piece, adj_pos[k])
        new_targ_piece = self.board[new_adj_pos[k][0]][new_adj_pos[k][1]]
        if (jumped_piece == opp_piece) and new_targ_piece == '-':
            #store as child node
            #make can jump more function
            child_board = self.get_board()
            child_board[new_adj_pos[k][0]][new_adj_pos[k][1]] = piece
            child_board[curr_pos[0]][curr_pos[1]] = '-'
            child_board[adj_pos[k][0]][adj_pos[k][1]] = '-'
            child = TreeNode(child_board, self, self.depth + 1)
            # child.can_jump(key, 'RIGHT', right_piece)
            return (True, child)
        return (False, None)

    def generate_child_moves(self):
        for i in range(8):
            for j in range(8):
                piece = self.board[i][j]
                if piece == None or piece == '-':
                    continue
                adj_pos = self.calc_adj_pos(piece, (i, j))
                for k in range(2):
                    if adj_pos[k] == None:
                        continue
                    targ_pos_y = adj_pos[k][0]
                    targ_pos_x = adj_pos[k][1]
                    targ_piece = self.board[targ_pos_y][targ_pos_x]
                    if targ_piece == piece:
                        continue
                    elif targ_piece == '-':
                        child = self.make_child([i,j], adj_pos[k])
                    else:
                        package = self.can_jump([i,j], adj_pos, k, targ_piece)
                        if package[0] == True:
                            package[1].set_parent(self)
                            self.set_children([package[1]])
                            # package = package[1].can_jump(piece, adj_pos, k, target_piece)
                    


        # def can_jump_more:
        #     for i in range(2):
        #         package = self.can_jump(piece, adj_pos, k, target_piece)

    
if __name__ == '__main__':
    root = TreeNode()
    root.display_board()
    root.generate_child_moves()
    print(len(root.children))
    for child in root.children:
        child.display_board()
        print('-----Next Board-----')
