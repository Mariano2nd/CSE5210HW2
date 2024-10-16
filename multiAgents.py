from GameStatus_5120 import GameStatus

# Imported the random library to choose a position in the event that
# two nodes being compared are of equal value
import random


def minimax(game_state: GameStatus, depth: int, maximizingPlayer: bool, alpha=float('-inf'), beta=float('inf')):
	
	# Obtains the T/F boolean value from the is_terminal() function
	terminal = game_state.is_terminal()
	
	# If we are at the end of our declared depth or the game is in a terminal state,
	# collect the score of the board and return it to the parent caller
	if (depth==0) or (terminal):
		newScores = game_state.get_scores(terminal)
		return newScores, None
	
	# This section of code is for our maximizing agent
	if maximizingPlayer:
		# The max evaluation is set to an arbitrary small value by default
		# so that the first value compared with it will take it's place 
		maxEval = float("-inf")
		# We obtain a list of available moves by calling the get_moves()
		# function in the GameStatus file
		availableMoves = game_state.get_moves()
		
		# Conduct the recursive calls that switch between the Max and Min
		# agents for each possible move on the board. The best move is checked
		# at each step by evaluating the corresponding game score.
		for position in availableMoves:
			# Pass in (depth - 1) to move down a level and "False" to give control
			# to the minimizing agent
			currEval = minimax(game_state, depth - 1, False, alpha, beta)[0]
			# If the current eval has a better score than our highest known score,
			# set the bestMove to the current position in the loop
			if currEval > maxEval:
				bestMove = position
				maxEval = currEval
				
			# Need to see if this approach is allowed / works	
			"""	
			# In the case that the two scores being compared are equal, the implication
			# is that both options lead to the same utility at the end of the game.
			# Rather than simply leaving the first node found as the chosen position,
			# the code below will randomly pick one of the two equal score positions
			elif currEval == maxEval:
				decision = random.choice([1, 2])
				if decision == 1:
					bestMove = position"""
					
					
			# alpha is set to the larger value between itself and the currEval.
			# Then, if the beta is <= alpha, the branch is pruned
			alpha = max(alpha, currEval)
			if beta <= alpha:
				break
			
		# Returns the best possible score for the maximizing agent and the corresponding move
		return maxEval, bestMove
			
			
	# This section of code is for our minimizing agent
	else:
		# The min evaluation is set to an arbitrary large value by default
		# so that the first value compared with it will take it's place 
		minEval = float("inf")
		# We obtain a list of available moves by calling the get_moves()
		# function in the GameStatus file
		availableMoves = game_state.get_moves()
		
		# Conduct the recursive calls that switch between the Max and Min
		# agents for each possible move on the board. The best move is checked
		# at each step by evaluating the corresponding game score.
		for position in availableMoves:
			# Pass in (depth - 1) to move down a level and "True" to give control
			# to the maximizing agent
			currEval = minimax(game_state, depth - 1, True, alpha, beta)[0]
			# If the current eval has a lower score than our lowest known score,
			# set the bestMove to the current position in the loop
			if currEval < minEval:
				bestMove = position
				minEval = currEval
				
			# Need to see if this approach is allowed / works	
			"""	
			# In the case that the two scores being compared are equal, the implication
			# is that both options lead to the same utility at the end of the game.
			# Rather than simply leaving the first node found as the chosen position,
			# the code below will randomly pick one of the two equal score positions
			elif currEval == minEval:
				decision = random.choice([1, 2])
				if decision == 1:
					bestMove = position"""
					
					
			# beta is set to the smaller value between itself and the currEval.
			# Then, if the beta is <= alpha, the branch is pruned
			beta = min(beta, currEval)
			if beta <= alpha:
				break
					
		# Returns the best possible score for the minimizing agent and the corresponding move
		return minEval, bestMove
				

	"""
    YOUR CODE HERE TO FIRST CHECK WHICH PLAYER HAS CALLED THIS FUNCTION (MAXIMIZING OR MINIMIZING PLAYER)
    YOU SHOULD THEN IMPLEMENT MINIMAX WITH ALPHA-BETA PRUNING AND RETURN THE FOLLOWING TWO ITEMS
    1. VALUE
    2. BEST_MOVE
    
    THE LINE TO RETURN THESE TWO IS COMMENTED BELOW WHICH YOU CAN USE
    """
	# Ended up doing return statements at the end of each for loop
	# return value, best_move

def negamax(game_state: GameStatus, depth: int, turn_multiplier: int, alpha=float('-inf'), beta=float('inf')):
	"""
    YOUR CODE HERE TO CALL NEGAMAX FUNCTION. REMEMBER THE RETURN OF THE NEGAMAX SHOULD BE THE OPPOSITE OF THE CALLING
    PLAYER WHICH CAN BE DONE USING -NEGAMAX(). THE REST OF YOUR CODE SHOULD BE THE SAME AS MINIMAX FUNCTION.
    YOU ALSO DO NOT NEED TO TRACK WHICH PLAYER HAS CALLED THE FUNCTION AND SHOULD NOT CHECK IF THE CURRENT MOVE
    IS FOR MINIMAX PLAYER OR NEGAMAX PLAYER
    RETURN THE FOLLOWING TWO ITEMS
    1. VALUE
    2. BEST_MOVE
    
    THE LINE TO RETURN THESE TWO IS COMMENTED BELOW WHICH YOU CAN USE
    
    """
    
    
	# Obtains the T/F boolean value from the is_terminal() function
	terminal = game_state.is_terminal()
		
	# If we are at the end of our declared depth or the game is in a terminal state,
	# collect the score of the board and return it to the parent caller
	if (depth==0) or (terminal):
		newScores = game_state.get_negamax_scores(terminal)
		return newScores, None
	

	# The max evaluation is set to an arbitrary small value by default
	# so that the first value compared with it will take it's place 
	maxEval = float("-inf")
	# We obtain a list of available moves by calling the get_moves()
	# function in the GameStatus file
	availableMoves = game_state.get_moves()
		
	# 
	for position in availableMoves:
		# Pass in (depth - 1) to move down a level and 
		currEval = -negamax(game_state, depth - 1, -turn_multiplier, -alpha, -beta)[0]
		# If the current eval has a better score than our highest known score,
		# set the bestMove to the current position in the loop
		if currEval > maxEval:
			bestMove = position
			maxEval = currEval
			
		# Need to see if this approach is allowed / works	
		"""	
		# In the case that the two scores being compared are equal, the implication
		# is that both options lead to the same utility at the end of the game.
		# Rather than simply leaving the first node found as the chosen position,
		# the code below will randomly pick one of the two equal score positions
		elif currEval == maxEval:
			decision = random.choice([1, 2])
			if decision == 1:
				bestMove = position"""
					
			
		# Returns the best possible score for the maximizing agent and the corresponding move
		return maxEval, bestMove