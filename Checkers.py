from Constants import empty, board
from Evaluation import evaluate

class TreeNode():
    def __init__(self, board = board, parent = None, depth = 6, children = [], value = None, maxTurn = True):
        self.board = board
        self.parent = parent
        self.depth = depth
        self.children = children
        self.value = value
        self.maxTurn = maxTurn
    
    #HELPER FUNCTIONS
    def get_board(self):
        return [row[:] for row in self.board]
    
    def get_children(self):
        return self.children[:]

    def set_children(self, childlist):
        if len(self.get_children()) == 0:
            self.children = childlist[:]
        else:
            self.children += childlist
    
    def set_parent(self, parent):
        self.parent = parent

    def set_board(self, board):
        self.board = board   
        
    def display_board(self):
        #displays the board funny
        print('-------Printing Board-------')
        for row in self.board:
            # print('[%s]' % ', '.join(map(str, row)))
            print(row)
        print('-----Finished Printing-----')

    def is_king(self, targ_pos, piece):
        if piece == 'r' and targ_pos[0] == 7:
            return True
        elif piece == 'b' and targ_pos[0] == 0:
            return True
        else:
            return False

    def calc_adj_pos(self, team, pos):
        newpos0 = [pos[0]-1, pos[1]-1]
        newpos1 = [pos[0]-1, pos[1]+1]
        newpos3 = [pos[0]+1, pos[1]-1]
        newpos4 = [pos[0]+1, pos[1]+1]
        adj_pos = [newpos0, newpos1, newpos3, newpos4]
        if team == 'r':
            adj_pos[0], adj_pos[1] = None, None
        elif team == 'b':
            adj_pos[2], adj_pos[3] = None, None
        for i in range(4):
            for j in range(2):
                if adj_pos[i] == None:
                    continue
                if adj_pos[i][j] < 0 or adj_pos[i][j] > 7:
                    adj_pos[i] = None
        return adj_pos

    def make_child(self, curr_pos, targ_pos):
        targ_pos_y = targ_pos[0]
        targ_pos_x = targ_pos[1]
        new_board = self.get_board()
        piece = self.board[curr_pos[0]][curr_pos[1]]
        if self.is_king((targ_pos_y, targ_pos_x), piece) == True:
            piece = piece.upper()
        new_board[curr_pos[0]][curr_pos[1]] = '-'
        new_board[targ_pos_y][targ_pos_x] = piece
        child_val = evaluate(new_board)
        child = TreeNode(new_board, self, self.depth - 1, value = child_val, maxTurn = not self.maxTurn)
        self.set_children([child])
        return child

    def choose_dir(self, pos):
        played_board = self.get_board()[:]
        piece = played_board[pos[0]][pos[1]]
        while True:
            dir_index = int(input('Direction (0-4):\n1       2\n    0    \n3       4\nPress "9" to reselect piece: '))
            adj_pos = self.calc_adj_pos(piece, [pos[0], pos[1]])
            if len(self.children) == 0:
                print('Sorry this piece cannot move. Please chose another piece')
            if dir_index == 9:
                break
            elif dir_index != 0:
                targ_pos = adj_pos[dir_index-1]
            for child in self.get_children():
                new_board = child.get_board()
                if new_board[pos[0]][pos[1]] != piece and new_board[targ_pos[0]][targ_pos[1]] != played_board[targ_pos[0]][targ_pos[1]]:
                    return child
            print('The direction you entered was invalid, please input another direction or try and move with a seperate piece')
            continue
    #END OF HELPER FUNCTIONS

    def can_jump(self, curr_pos, adj_pos, k, jumped_piece):
        #where k is the direction index
        piece = self.board[curr_pos[0]][curr_pos[1]]
        if piece.lower() == 'r':
            opp_piece = 'b'
        elif piece.lower() == 'b':
            opp_piece = 'r'
        new_adj_pos = self.calc_adj_pos(piece, adj_pos[k])
        if new_adj_pos[k] == None:
            return (False, None)
        new_targ_piece = self.board[new_adj_pos[k][0]][new_adj_pos[k][1]]
        if (jumped_piece.lower() == opp_piece) and new_targ_piece == '-':
            #make can jump more function
            child_board = self.get_board()
            child_board[new_adj_pos[k][0]][new_adj_pos[k][1]] = piece
            child_board[curr_pos[0]][curr_pos[1]] = '-'
            child_board[adj_pos[k][0]][adj_pos[k][1]] = '-'
            child_val = evaluate(child_board)
            child = TreeNode(child_board, self, self.depth - 1, value = child_val, maxTurn = not self.maxTurn)
            return (True, child, [new_adj_pos[k][0], new_adj_pos[k][1]])
        return (False, None, None)             

    def can_jump_more(self, piece, curr_pos):
        pass
    
    def generate_child_moves(self, team):
        for i in range(8):
            for j in range(8):
                piece = self.board[i][j]
                if piece == None or piece == '-':
                    continue
                if piece.lower() == team:
                    adj_pos = self.calc_adj_pos(piece, (i, j))
                    for k in range(4): #k is the direction index
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
                                child = package[1]
                                child.value = evaluate(child.get_board())
                                child.set_parent(self)
                                self.set_children([child])
                                child.can_jump_more(piece, package[2])

    def input_board_position(self, player_ismin):
        '''
        Allows user interactivity with the tic tac toe board
        User specifies which position they would like to chose
        Return the corresponding child TreeNode object
        '''
        if player_ismin:
            team = 'b'
        else:
            team = 'r'
        if len(self.children) == 0:
            self.generate_child_moves(team)
        while True:
            print('-----please specify the piece you would like to move-----')
            column = int(input('Column (1-8): '))
            row = int(input('Row (1-8): '))
            played_board = self.get_board()[:]
            piece = played_board[row-1][column-1]
            if piece == None:
                print('sorry you selected an invalid square')
                continue
            elif piece.lower() != team:
                print('Sorry, the slot you selected as your character piece is either occupied by an enemy piece, empty or does not exist. Try again')
                continue
            print('-----Thank you-----')
            child = self.choose_dir([row-1, column-1])
            if child == None:
                continue
            return child

    def select_team(self):
        while True:
            player_team = input('Please input which team you would like to play for ("R" or "B"): ').lower()
            if player_team.upper() == 'R' or player_team.upper() == 'B':
                break
            print('Please try again and input a valid team ("R" or "B")')
        return player_team

    def minimax(self, depth = 6):
        if depth == 0 or self.value == 1000 or self.value == -1000:
            return self, self.value
        
        if self.maxTurn:
            self.generate_child_moves('r')
            max_board_val = None, -10000
            for child in self.get_children():
                tboard_eval = child.minimax(depth - 1)[1]
                if tboard_eval > max_board_val[1]:
                    max_board_val = child, tboard_eval  
            self.value = max_board_val[1]
            return max_board_val
        
        else:
            self.generate_child_moves('b')
            min_board_val = None, 10000
            for child in self.get_children():
                tboard_eval = child.minimax(depth - 1)[1]
                if tboard_eval < min_board_val[1]:
                    min_board_val = child, tboard_eval
            self.value = min_board_val[1]
            return min_board_val  

    def play_game(self, aiismax):
        '''
        Allows the user and the AI to play a game of tic tac toe
        If the ai is the maximizing player and it is the maximizing player's turn to move then, 
        The AI uses the make_move and minimax function to chose the ideal child node
        After the turn switches and the user specifies his best move, if the users move was not 
            already predicted by the minimax algorithm then we need to recalculate the ideal route
        '''
        state = self
        while self.value != 1000 and self.value != -1000:
            state.display_board()
            if (aiismax == state.maxTurn):
                state = state.minimax()[0]
            else:
                state = state.input_board_position(aiismax)
                state.depth = minimax_depth = 6
                state.children = []

                
        return state.end_game()
        
    def end_game(self):
        print('-----Game Over-----')
        self.display_board()
        if self.value == 1000:
            print('Red Team Won!!')
        elif self.value == -1000:
            print('Black Team Won!!')
        while True:
            decision = input("Would you like to play again (y/N): ")
            if decision == 'y':
                return True
            elif decision == 'N':
                return False
            print('Please input a valid expression')

    
if __name__ == '__main__':
    minimax_depth = 6
    root = TreeNode(board)

    play = True
    while True:
        player_team = root.select_team()
        play = root.play_game((player_team.upper() == "B"))
    print('Thank you for playing')


