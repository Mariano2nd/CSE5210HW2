"""
PLEASE READ THE COMMENTS BELOW AND THE HOMEWORK DESCRIPTION VERY CAREFULLY BEFORE YOU START CODING

 The file where you will need to create the GUI which should include (i) drawing the grid, (ii) call your Minimax/Negamax functions
 at each step of the game, (iii) allowing the controls on the GUI to be managed (e.g., setting board size, using 
                                                                                 Minimax or Negamax, and other options)
 In the example below, grid creation is supported using pygame which you can use. You are free to use any other 
 library to create better looking GUI with more control. In the __init__ function, GRID_SIZE (Line number 36) is the variable that
 sets the size of the grid. Once you have the Minimax code written in multiAgents.py file, it is recommended to test
 your algorithm (with alpha-beta pruning) on a 3x3 GRID_SIZE to see if the computer always tries for a draw and does 
 not let you win the game. Here is a video tutorial for using pygame to create grids http://youtu.be/mdTeqiWyFnc
 
 
 PLEASE CAREFULLY SEE THE PORTIONS OF THE CODE/FUNCTIONS WHERE IT INDICATES "YOUR CODE BELOW" TO COMPLETE THE SECTIONS
 
"""
import pygame
import numpy as np
from GameStatus_5120 import GameStatus
from multiAgents import minimax, negamax
import sys, random

mode = "player_vs_ai" # default mode for playing the game (player vs AI)

class RandomBoardTicTacToe:
    def __init__(self, size = (600, 600)):

        self.size = self.width, self.height = size
        # Define some colors
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.GREEN = (0, 255, 0)
        self.RED = (255, 0, 0)

        # Grid Size
        self.GRID_SIZE = 3
        self.OFFSET = 5

        self.CIRCLE_COLOR = (140, 146, 172)
        self.CROSS_COLOR = (140, 146, 172)

        # This sets the WIDTH and HEIGHT of each grid location
        self.WIDTH = self.size[0]/self.GRID_SIZE - self.OFFSET
        self.HEIGHT = self.size[1]/self.GRID_SIZE - self.OFFSET

        # This sets the margin between each cell
        self.MARGIN = 5

        # Initialize pygame
        self.reset_true = True
        self.board_state = [[0 for i in range(self.GRID_SIZE)] for i in range(self.GRID_SIZE)]
        while self.reset_true:
            print('gameloop start')
            if pygame.get_init():
                self.play_game()
            else:
                self.game_reset()
            print('gameloop end')
            print('2 reset_true?',self.reset_true)

    def draw_game(self):
        # Create a 2 dimensional array using the column and row variables
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption(f"Tic Tac Toe Random Grid {'- Player vs Player' if self.mode == 'player_vs_player' else ' - click anywhere for ai to place move' if self.game_state.turn_O != self.player_is else ' - Player vs ai'}")
        self.screen.fill(self.BLACK)
        # Draw the grid
        
        """
        YOUR CODE HERE TO DRAW THE GRID OTHER CONTROLS AS PART OF THE GUI
        """
        for row in range(self.GRID_SIZE):
            for col in range(self.GRID_SIZE):
                pygame.draw.rect(self.screen,self.WHITE,pygame.Rect((self.WIDTH+self.MARGIN)*row+self.MARGIN,(self.HEIGHT+self.MARGIN)*col+self.MARGIN,self.WIDTH-self.MARGIN,self.HEIGHT-self.MARGIN))
                
        #print('check game board')
        # pygame.display.update()
        
    def change_turn(self):
        if(self.game_state.turn_O):
            pygame.display.set_caption(f"Tic Tac Toe - O's turn {'' if self.mode == 'player_vs_player' else '(click for ai)'}")
        else:
            pygame.display.set_caption(f"Tic Tac Toe - X's turn {'' if self.mode == 'player_vs_player' else '(click for ai)'}")
        # print('Check before changing turn O',self.game_state.turn_O)
        # #input()
        # self.game_state.turn_O = not self.game_state.turn_O
        # print('Check after changing turn O',self.game_state.turn_O)
        # #input()


    def draw_circle(self, x, y):
        """
        YOUR CODE HERE TO DRAW THE CIRCLE FOR THE NOUGHTS PLAYER
        """
        print("Check x and y", x, y)
        center = ((self.HEIGHT+self.MARGIN)*x + self.WIDTH/2,(self.WIDTH+self.MARGIN)*y + self.HEIGHT/2) #in my mind since the rectangle dimensions are width or height minus margin
        radius = self.WIDTH // 3
        pygame.draw.circle(self.screen,self.CIRCLE_COLOR,center,radius,5)
        print('Check draw circle')
        # #input()
        # pygame.display.update()

    def draw_cross(self, x, y):
        """
        YOUR CODE HERE TO DRAW THE CROSS FOR THE CROSS PLAYER AT THE CELL THAT IS SELECTED VIA THE gui
        """
        print('Check draw cross')
        font = pygame.font.SysFont('arial', 150)
        text = font.render('X', True, self.BLACK, self.WHITE)
        self.thedisplay.blit(text, ((self.WIDTH+self.MARGIN)*x + self.MARGIN+50,(self.HEIGHT+self.MARGIN)*y+25))
        # pygame.display.update()

    def is_game_over(self):

        """
        YOUR CODE HERE TO SEE IF THE GAME HAS TERMINATED AFTER MAKING A MOVE. YOU SHOULD USE THE IS_TERMINAL()
        FUNCTION FROM GAMESTATUS_5120.PY FILE (YOU WILL FIRST NEED TO COMPLETE IS_TERMINAL() FUNCTION)
        
        YOUR RETURN VALUE SHOULD BE TRUE OR FALSE TO BE USED IN OTHER PARTS OF THE GAME
        """
        game_over = self.game_state.is_terminal()
        #print('Check game over')
        return game_over
    

    def move(self, move):
        print('Check move')
        self.game_state = self.game_state.get_new_state(move)
        print("game state",self.game_state.board_state)


    def play_ai(self):
        """
        YOUR CODE HERE TO CALL MINIMAX OR NEGAMAX DEPENDEING ON WHICH ALGORITHM SELECTED FROM THE GUI
        ONCE THE ALGORITHM RETURNS THE BEST MOVE TO BE SELECTED, YOU SHOULD DRAW THE NOUGHT (OR CIRCLE DEPENDING
        ON WHICH SYMBOL YOU SELECTED FOR THE AI PLAYER)
        
        THE RETURN VALUES FROM YOUR MINIMAX/NEGAMAX ALGORITHM SHOULD BE THE SCORE, MOVE WHERE SCORE IS AN INTEGER
        NUMBER AND MOVE IS AN X,Y LOCATION RETURNED BY THE AGENT
        """
        print('Check play ai')
        tempgamestate = self.game_state
        if mode == "player_vs_ai":
            score, move = minimax(tempgamestate, 4, True)
            print('minmax value: ',score,move)
        elif mode == "negamax":
            score, move = negamax(tempgamestate, 4, True)
            print('negamax value: ', score,move)
        print('ai move',move, 'and score is',score)
        return move

        """ USE self.game_state.get_scores(terminal) HERE TO COMPUTE AND DISPLAY THE FINAL SCORES """



    def game_reset(self):
        """
        YOUR CODE HERE TO RESET THE BOARD TO VALUE 0 FOR ALL CELLS AND CREATE A NEW GAME STATE WITH NEWLY INITIALIZED
        BOARD STATE
        """
        self.reset_true = False
        for i in range(len(self.board_state)):
            for j in range(len(self.board_state[i])):
                self.board_state[i][j]=0
        self.thedisplay=pygame.display.set_mode(self.size)
        if not pygame.get_init():
            self.play_game()
        print('Check game reset')
        

    def play_game(self, mode = "player_vs_ai"):
        done = False
        print('pygame initing')
        if not pygame.get_init():
            pygame.init()
        print('pygame after init')
        # self.board_state = [[0 for i in range(3)] for i in range(3)]
        # prompt the player for choice: O is first, X goes second ALWAYS
        font = pygame.font.SysFont('arial', 32)
        text = font.render('O always goes first, press', True, self.BLACK, self.WHITE)
        pygame.display.set_caption('Choose O or X')
        self.thedisplay.blit(text, (0, self.height // 2))
        text = font.render(' [1] for O and [2] for X', True, self.BLACK, self.WHITE)
        self.thedisplay.blit(text, (0, self.height // 2 + 40))
        # game mode
        text = font.render(f'Current game mode: {mode}', True, self.BLACK, self.WHITE)
        self.mode = mode
        self.thedisplay.blit(text, (0, self.height // 2 + 100))
        self.player_is = None
        pygame.display.update()
        while self.player_is == None:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    
                    if event.key == pygame.K_1:
                        self.player_is = True# O
                        print('player is O')
                    elif event.key == pygame.K_2:
                        self.player_is = False#  X
                        print('player is X')
                    if event.key == pygame.K_m:
                        if mode == 'player_vs_player':
                            self.mode = 'player_vs_ai'
                        else:
                            self.mode = 'player_vs_player'
                        mode = self.mode
                        pygame.draw.rect(self.thedisplay,self.BLACK,pygame.Rect(300, self.height // 2 + 100, 300, 40))
                        pygame.display.update()
                        text = font.render(f'Current game mode: {self.mode}', True, self.BLACK, self.WHITE)
                        self.thedisplay.blit(text, (0, self.height // 2 + 100))
                        pygame.display.update()
                #print('capture key press')
            #print('check 0.5:',self.player_is)
        # #input()
        self.game_state = GameStatus(self.board_state, True)
        self.draw_game()

        clock = pygame.time.Clock()
        pygame.display.update()
        

        #print('check1')
        while not done:
            #print('check2',self.game_state.turn_O)
            for event in pygame.event.get():  # User did something
                """
                YOUR CODE HERE TO CHECK IF THE USER CLICKED ON A GRID ITEM. EXIT THE GAME IF THE USER CLICKED EXIT
                """
                #print('check3')
                if event.type == pygame.QUIT:
                    #print('check3.1')
                    done = True
                """
                YOUR CODE HERE TO HANDLE THE SITUATION IF THE GAME IS OVER. IF THE GAME IS OVER THEN DISPLAY THE SCORE,
                THE WINNER, AND POSSIBLY WAIT FOR THE USER TO CLEAR THE BOARD AND START THE GAME AGAIN (OR CLICK EXIT)
                """
                #print('check4')
                # TODOs: (1) Display "Game is Over" (2) Display the score (3) Display the Winner -> "Black" or "White"
                #   (4) Display functional options/buttons to "Play Again" or (5) "Exit"
                
                if self.is_game_over():
                    # (4) & (5)
                    font = pygame.font.SysFont('arial', 32)
                    text = font.render('Game is Over', True, self.BLACK, self.WHITE)
                    pygame.display.set_caption('Game Over')
                    self.thedisplay.blit(text, (self.width // 2, self.height // 2))
                    text = font.render(f'Score is {self.game_state.get_scores(True)}', True, self.BLACK, self.WHITE)
                    self.thedisplay.blit(text, (self.width // 2, self.height // 2 + 50))
                    text = font.render(f'Restart board press [R]', True, self.BLACK, self.WHITE)
                    self.thedisplay.blit(text, (0, self.height // 2 + 100))
                    if event.type == pygame.KEYUP:
                        if self.is_game_over() and event.key == pygame.K_r:
                            print("Check reset board")
                            # #input()
                            self.game_reset()
                            self.reset_true = True
                            print('1 reset_true?',self.reset_true)
                            return

                    # game_reset here


                """
                YOUR CODE HERE TO NOW CHECK WHAT TO DO IF THE GAME IS NOT OVER AND THE USER SELECTED A NON EMPTY CELL
                IF CLICKED A NON EMPTY CELL, THEN GET THE X,Y POSITION, SET ITS VALUE TO 1 (SELECTED BY HUMAN PLAYER),
                DRAW CROSS (OR NOUGHT DEPENDING ON WHICH SYMBOL YOU CHOSE FOR YOURSELF FROM THE gui) AND CALL YOUR 
                PLAY_AI FUNCTION TO LET THE AGENT PLAY AGAINST YOU
                """
                #print('check5')
                if event.type == pygame.MOUSEBUTTONUP:
                    # Get the position
                    x, y = pygame.mouse.get_pos()
                    
                    # Change the x/y screen coordinates to grid coordinates
                    # print('WIDTH ', self.WIDTH, ' and HEIGHT ', self.HEIGHT)
                    pos_x = int(x / (self.WIDTH + self.MARGIN))
                    pos_y = int(y / (self.HEIGHT + self.MARGIN))
                    
                    # 1 - Check if the game is human vs human or human vs AI player from the GUI. 
                    # If it is human vs human then your opponent should have the value of the selected cell set to -1
                    # 2 - Then draw the symbol for your opponent in the selected cell
                    # xx- Within this code portion, continue checking if the game has ended by using is_terminal function
                    # 3 - check if move exists
                    # 3 - check if move exists
                    if (pos_x,pos_y) in self.game_state.get_moves():
                        # print('O' if self.game_state.turn_O else 'X',' must choose a different move')
                        # pygame.display.set_caption(f"{'O' if self.game_state.turn_O else 'X'} - must choose a different move")
                        continue# do not overwrite existing move



                    # 2 - draw respective symbol
                    # print("Check 2 of pos_x and pos_y:", pos_x, pos_y)
                    if self.game_state.turn_O:
                        self.draw_circle(pos_x, pos_y)
                    else:
                        self.draw_cross(pos_x, pos_y)
                    # #input()
                    self.move([pos_x, pos_y])
                    self.change_turn()

                    # 1 - write move onto board from ai or player
                    # print('player pos x and y', pos_x, pos_y)
                    # if ai's turn write move
                    print('is it ais turn?')
                    if self.mode == 'player_vs_ai' and not self.game_state.is_terminal():
                        print('check for ai turn',self.game_state.is_terminal())
                        if self.player_is != self.game_state.turn_O:
                            # print("game state before AI →", self.game_state.board_state)
                            print('\tai''s turn')

                            pos_x, pos_y = self.play_ai()
                            # print('position x and y →',pos_x,pos_y)
                            # print("game state after AI →", self.game_state.board_state)
                            for i in self.game_state.board_state:
                                for j in i:
                                    print(j)
                            #input()
                    # otherwise write player's move

                            # 2 - draw respective symbol
                            # print("Check 2 of pos_x and pos_y:", pos_x, pos_y)
                            if self.game_state.turn_O:
                                self.draw_circle(pos_x, pos_y)
                            else:
                                self.draw_cross(pos_x, pos_y)
                            # #input()
                            self.move([pos_x, pos_y])
                            self.change_turn()

                    
                    
                
                # if event.type == pygame.MOUSEBUTTONUP:
                #     # Get the position
                    
                #     # Change the x/y screen coordinates to grid coordinates
                    
                #     # Check if the game is human vs human or human vs AI player from the GUI. 
                #     # If it is human vs human then your opponent should have the value of the selected cell set to -1
                #     # Then draw the symbol for your opponent in the selected cell
                #     # Within this code portion, continue checking if the game has ended by using is_terminal function
                #     pygame.mouse.get_pos
                    
            # Update the screen with what was drawn.
            pygame.display.update()

        pygame.quit()

tictactoegame = RandomBoardTicTacToe()
# tictactoegame.play_game()
"""
YOUR CODE HERE TO SELECT THE OPTIONS VIA THE GUI CALLED FROM THE ABOVE LINE
AFTER THE ABOVE LINE, THE USER SHOULD SELECT THE OPTIONS AND START THE GAME. 
YOUR FUNCTION PLAY_GAME SHOULD THEN BE CALLED WITH THE RIGHT OPTIONS AS SOON
AS THE USER STARTS THE GAME
"""
