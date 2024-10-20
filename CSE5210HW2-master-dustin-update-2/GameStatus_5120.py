# -*- coding: utf-8 -*-


class GameStatus:


	def __init__(self, board_state, turn_O):

		self.board_state = board_state.copy()
		self.turn_O = turn_O
		self.oldScores = 0

		self.winner = ""


	def is_terminal(self):
		"""
        YOUR CODE HERE TO CHECK IF ANY CELL IS EMPTY WITH THE VALUE 0. IF THERE IS NO EMPTY
        THEN YOU SHOULD ALSO RETURN THE WINNER OF THE GAME BY CHECKING THE SCORES FOR EACH PLAYER 
        """
		rows = len(self.board_state)
		cols = len(self.board_state[0])
		terminal = True

		# Loop through the board state and check if there is an empty square
		for i in range(rows):
			for j in range(cols):
				if self.board_state[i][j] == 0:
					terminal = False
					return terminal

		#Return the results
		self.get_scores(terminal)
		return terminal
		

	def get_scores(self, terminal):
		"""
        YOUR CODE HERE TO CALCULATE THE SCORES. MAKE SURE YOU ADD THE SCORE FOR EACH PLAYER BY CHECKING 
        EACH TRIPLET IN THE BOARD IN EACH DIRECTION (HORIZONAL, VERTICAL, AND ANY DIAGONAL DIRECTION)
        
        YOU SHOULD THEN RETURN THE CALCULATED SCORE WHICH CAN BE POSITIVE (HUMAN PLAYER WINS),
        NEGATIVE (AI PLAYER WINS), OR 0 (DRAW)
        
        """        
		rows = len(self.board_state)
		cols = len(self.board_state[0])
		scores = 0
		check_point = 3 if terminal else 2
        
        # Check all of the rows in the board
        # Only goes up to the length of rows - 2 to prevent an error from being out of the array's bounds
		
		for row in range(rows):
			for col in range(cols - 2):
                # If we encounter an unplayed position, skip it because it wont be one of the three characters
                # needed to score the player or AI a point.
				if self.board_state[row][col] == 0:
					break
				elif self.board_state[row][col] == self.board_state[row][col + 1] == self.board_state[row][col + 2]:
					scores = scores + self.board_state[row][col]
				
        # Check all of the columns in the board
        # Only goes up to the length of columns - 2 to prevent an error from being out of the array's bounds
				
		for row in range(rows - 2):
			for col in range(cols):
                # If we encounter an unplayed position, skip it because it wont be one of the three characters
                # needed to score the player or AI a point.
				if self.board_state[row][col] == 0:
					break
				elif self.board_state[row][col] == self.board_state[row + 1][col] == self.board_state[row + 2][col]:
					scores = scores + self.board_state[row][col]

				
		# Check all of the diagonal positions in the board
        # Basically only searches the indices where 3 consecutive diagonal positions are possible. In a 3x3 grid,
		# this would be the top left and bottom left position. In a 4x4 grid this is the top 2x2 subsection of the grid 
		# and the bottom 2x2 subsection of the grid.
				
		# Checks from the top left
		for row in range(rows - 2):
			for col in range(cols - 2):
                # If we encounter an unplayed position, skip it because it wont be one of the three characters
                # needed to score the player or AI a point.
				if self.board_state[row][col] == 0:
					break
				elif self.board_state[row][col] == self.board_state[row + 1][col + 1] == self.board_state[row + 2][col + 2]:
					scores = scores + self.board_state[row][col]
				
		# Checks from the bottom left
		for row in range(2, rows):
			for col in range(cols - 2):
                # If we encounter an unplayed position, skip it because it wont be one of the three characters
                # needed to score the player or AI a point.
				if self.board_state[row][col] == 0:
					break
				elif self.board_state[row][col] == self.board_state[row - 1][col + 1] == self.board_state[row - 2][col + 2]:
					scores = scores + self.board_state[row][col]

				
		return scores
		
	    

	def get_negamax_scores(self, terminal):
		"""
        YOUR CODE HERE TO CALCULATE NEGAMAX SCORES. THIS FUNCTION SHOULD EXACTLY BE THE SAME OF GET_SCORES UNLESS
        YOU SET THE SCORE FOR NEGAMX TO A VALUE THAT IS NOT AN INCREMENT OF 1 (E.G., YOU CAN DO SCORES = SCORES + 100 
                                                                               FOR HUMAN PLAYER INSTEAD OF 
                                                                               SCORES = SCORES + 1)
        """
		rows = len(self.board_state)
		cols = len(self.board_state[0])
		scores = 0
		check_point = 3 if terminal else 2
		
        # Check all of the rows in the board
        # Only goes up to the length of rows - 2 to prevent an error from being out of the array's bounds
		
		for row in range(rows):
			for col in range(cols - 2):
                # If we encounter an unplayed position, skip it because it wont be one of the three characters
                # needed to score the player or AI a point.
				if self.board_state[row][col] == 0:
					break
				elif self.board_state[row][col] == self.board_state[row][col + 1] == self.board_state[row][col + 2]:
					scores = scores + self.board_state[row][col]
	
        # Check all of the columns in the board
        # Only goes up to the length of columns - 2 to prevent an error from being out of the array's bounds
				
		for row in range(rows - 2):
			for col in range(cols):
                # If we encounter an unplayed position, skip it because it wont be one of the three characters
                # needed to score the player or AI a point.
				if self.board_state[row][col] == 0:
					break
				elif self.board_state[row][col] == self.board_state[row + 1][col] == self.board_state[row + 2][col]:
					scores = scores + self.board_state[row][col]
	
		# Check all of the diagonal positions in the board
        # Basically only searches the indices where 3 consecutive diagonal positions are possible. In a 3x3 grid,
		# this would be the top left and bottom left position. In a 4x4 grid this is the top 2x2 subsection of the grid 
		# and the bottom 2x2 subsection of the grid.
				
		# Checks from the top left
		for row in range(rows - 2):
			for col in range(cols - 2):
                # If we encounter an unplayed position, skip it because it wont be one of the three characters
                # needed to score the player or AI a point.
				if self.board_state[row][col] == 0:
					break
				elif self.board_state[row][col] == self.board_state[row + 1][col + 1] == self.board_state[row + 2][col + 2]:
					scores = scores + self.board_state[row][col]
			
				
		# Checks from the bottom left
		for row in range(2, rows):
			for col in range(cols - 2):
                # If we encounter an unplayed position, skip it because it wont be one of the three characters
                # needed to score the player or AI a point.
				if self.board_state[row][col] == 0:
					break
				elif self.board_state[row][col] == self.board_state[row - 1][col + 1] == self.board_state[row - 2][col + 2]:
					scores = scores + self.board_state[row][col]
				
		return scores
	    

	def get_moves(self):
		moves = []
		"""
		YOUR CODE HERE TO ADD ALL THE NON EMPTY CELLS TO MOVES VARIABLES AND RETURN IT TO BE USE BY YOUR
		MINIMAX OR NEGAMAX FUNCTIONS
		"""
		rows = len(self.board_state)
		cols = len(self.board_state[0])

		# Loop through board_state and add empty cells to moves
		for i in range(rows):
			for j in range(cols):
				if self.board_state[i][j] != 0:
					moves.append((i,j))
		# print(moves)
		return moves


	def get_new_state(self, move):
		new_board_state = []
		for i in self.board_state:
			row = []
			for j in i:
				row.append(j)
			new_board_state.append(row)
		x, y = move[0], move[1]
		new_board_state[x][y] = 1 if self.turn_O else -1# -1 is X, 1 is O
		return GameStatus(new_board_state, not self.turn_O)


