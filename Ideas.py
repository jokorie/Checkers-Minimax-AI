
# board = [['-', None, '-', None, '-', None, '-', None],
#          [None, '-', None, '-', None, '-', None, '-'],
#          ['-', None, '-', None, '-', None, '-', None],
#          [None, '-', None, '-', None, '-', None, '-'],
#          ['-', None, '-', None, '-', None, '-', None],
#          [None, '-', None, '-', None, '-', None, '-'],
#          ['-', None, '-', None, '-', None, '-', None],
#          [None, '-', None, '-', None, '-', None, '-']]

# board = [['r01', None, 'r02', None, 'r03', None, 'r04', None],
#          [None, 'r05', None, 'r06', None, 'r07', None, 'r08'],
#          ['r09', None, 'r10', None, 'r11', None, 'r12', None],
#          [None, '-', None, '-', None, '-', None, '-'],
#          ['-', None, '-', None, '-', None, '-', None],
#          [None, 'b09', None, 'b10', None, 'b11', None, 'b12'],
#          ['b05', None, 'b06', None, 'b07', None, 'b08', None],
#          [None, 'b01', None, 'b02', None, 'b03', None, 'b04']]
                        

    # def check_left(self):
    #     for key in self.pos:
    #         piece = self.pos[key][0]
    #         #make a check left position method
    #         left_piece = self.pos[self.pos[key][1][0]][0]
    #         assert piece == 'b' or piece == 'r' or piece == '-'
    #         if left_piece == piece: 
    #             #left accessible position occupied by same team piece
    #             continue
    #         if left_piece == '-':
    #             self.make_child(self.pos, piece, 'LEFT')
    #             #left accessible open position
    #             #store as child board
                

    # def check_right(self):
    #     for key in self.pos:
    #         piece = self.pos[key][0]
    #         #make a check  right position method
    #         right_piece = self.pos[self.pos[key][1][0]][1]
    #         assert piece == 'b' or piece == 'r' or piece == '-'
    #         if right_piece == piece:
    #             #right accessible position occupied by same team piece
    #             continue
    #         if right_piece == '-':
    #             #right accessible open position
    #             #store as child board
    #             self.make_child(self.pos, piece, 'LEFT')
    # if dir == 'LEFT':
    #         if (jumped_piece == opp_piece) and self.pos[self.pos[self.pos[key][1][0]][1][0]][0] == '-':
    #             #store as child node
    #             #make can jump more function
    #             new_pos = self.get_pos(self.pos)
    #             new_pos[self.pos[key][1][0]][0] = piece
    #             new_pos[key][0] = '-'
    #             child = TreeNode(new_pos, self, self.depth + 1)
    #             # child.can_jump(key, 'RIGHT', right_piece)
    #             return (True, child)

    #     elif dir == 'RIGHT':
    #         if (jumped_piece == opp_piece) and self.pos[self.pos[self.pos[key][1][1]][1][1]][0] == '-':
    #             #store as child node
    #             #make can jump more function
    #             new_pos = self.get_pos(self.pos)
    #             new_pos[self.pos[key][1][1]][0] = piece
    #             new_pos[key][0] = '-'
    #             child = TreeNode(new_pos, self, self.depth + 1)
    #             # child.can_jump(key, 'RIGHT', right_piece)
    #             return (True, child)