# Checkers-Minimax-AI
# Project Overview
Uses minimax algorithm to calculate an optimal move for checkers

# Detailed Description
- Minimax is a famous decision making algorithm which works with two-player turn-based perfect information games. In a proper implementation, every possible game state is represented as a node in a binary tree, whereas the root node is the starting game state where all other possible game states are fundamentally derived from. 
- When it is a players turn, that is represented as the player being in the node which corresponds to the active game state (prior to making a move). We represent all possible moves that a player can make as the offspring child nodes of the active node. In a typical game of minima, as you traverse the depth of the tree by one level, the turns alternate, ie... after player 1 makes a move it is now player 2's turn.

# Evaluation
- One requisite to the minimiax algorithm is an evaluation function, which can evaluate the current state of the board as favoring either P1 (player 1) or P2 (player 2). For the checkers implementation, I made the evaluation dependent on the number of checkers pieces left on each team with a harsher weighting on when there were less pieces on the board. In other words an advantage of one piece when there are 2 pieces left on the board is better than an advantage of 1 piece when there are 10 pieces left on the board.
- We will attribute a large possitive number as being an advantageous possitioning for P1 and a large negative number as being a favorable possitioning for P2. For this reason, we refer to P1 as being the maximizing player as it is attempting to chose a positioning which maximizies the score of its node. Likewise, we will refer to player 2 as being the minimizing player for similar reasons.

