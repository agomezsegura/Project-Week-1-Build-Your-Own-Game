#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pygame;
from pygame.locals import *
from pgu import engine
import random
import time
import game_board


# In[ ]:


##------------------------------------------------------Player_vs_Player screen ---------------------------------
class PlayerVSPlayer(engine.State):
    def init(self):
        self.board = pygame.image.load("im&font/board.png")
        
        #Initiate the sprites
        self.cells = game_board.GameBoard()
                
#        self.sel_cell=pygame.sprite.GroupSingle()
        
        self.turn = random.choice([1,2])
        self.finish = False
        self.result = ''
        self._init = 0
    
    def paint(self, s):
        s.fill((0, 0, 0))
        board_rect = self.board.get_rect()
        board_rect.center = s.get_rect().center
        s.blit(self.board, board_rect)
    
    def switch_turn(self):
        self.actual_time=pygame.time.get_ticks()
        if self.turn==2:
            self.turn=1
        else:
            self.turn+=1
            self.actual_time=pygame.time.get_ticks()
            
    def final(self):
        if (self.cells.matrix[0] == self.cells.matrix[1] and self.cells.matrix[0] == self.cells.matrix[2]) and self.cells.matrix[0] !='empty' and not self.finish:
            self.finish = True
            if self.cells.matrix[0] == 'circle':
                self.game.result = 'Player 1 wins'
            else:
                self.game.result = 'Player 2 wins'
        elif (self.cells.matrix[3] == self.cells.matrix[4] and self.cells.matrix[3] == self.cells.matrix[5]) and self.cells.matrix[3] !='empty' and not self.finish:
            self.finish = True
            if self.cells.matrix[3] == 'circle':
                self.game.result = 'Player 1 wins'
            else:
                self.game.result = 'Player 2 wins'
        elif (self.cells.matrix[6] == self.cells.matrix[7] and self.cells.matrix[6] == self.cells.matrix[8]) and self.cells.matrix[6] !='empty' and not self.finish:
            self.finish = True
            if self.cells.matrix[6] == 'circle':
                self.game.result = 'Player 1 wins'
            else:
                self.game.result = 'Player 2 wins'
        elif (self.cells.matrix[0] == self.cells.matrix[3] and self.cells.matrix[0] == self.cells.matrix[6]) and self.cells.matrix[0] !='empty' and not self.finish:
            self.finish = True
            if self.cells.matrix[0] == 'circle':
                self.game.result = 'Player 1 wins'
            else:
                self.game.result = 'Player 2 wins'
        elif (self.cells.matrix[1] == self.cells.matrix[4] and self.cells.matrix[1] == self.cells.matrix[7]) and self.cells.matrix[1] !='empty' and not self.finish:
            self.finish = True
            if self.cells.matrix[1] == 'circle':
                self.game.result = 'Player 1 wins'
            else:
                self.game.result = 'Player 2 wins'
        elif (self.cells.matrix[2] == self.cells.matrix[5] and self.cells.matrix[2] == self.cells.matrix[8]) and self.cells.matrix[2] !='empty' and not self.finish:
            self.finish = True
            if self.cells.matrix[2] == 'circle':
                self.game.result = 'Player 1 wins'
            else:
                self.game.result = 'Player 2 wins'
        elif (self.cells.matrix[0] == self.cells.matrix[4] and self.cells.matrix[0] == self.cells.matrix[8]) and self.cells.matrix[0] !='empty' and not self.finish:
            self.finish = True
            if self.cells.matrix[0] == 'circle':
                self.game.result = 'Player 1 wins'
            else:
                self.game.result = 'Player 2 wins'
        elif (self.cells.matrix[2] == self.cells.matrix[4] and self.cells.matrix[2] == self.cells.matrix[6]) and self.cells.matrix[2] !='empty' and not self.finish:
            self.finish = True
            if self.cells.matrix[2] == 'circle':
                self.game.result = 'Player 1 wins'
            else:
                self.game.result = 'Player 2 wins'
        if 'empty' not in self.cells.matrix:
            if self.result == 'First check done':
                self.final()
                self.game.result = 'DrawPvP'
                self.finish = True
            else:
                self.result = 'Firs check done'
            
    def event(self,event):
        if event.type is KEYDOWN:
            if event.key == K_q:
                return self.game.change_state('EXIT')
        elif event.type is pygame.MOUSEBUTTONDOWN:
            if self.turn==1:
                if (event.pos[0]<=250 and event.pos[1]<=250) and self.cells.matrix[0] == 'empty':
                    self.cell1 = game_board.GameBoardCell(0,'circle')
                    self.cells.add(self.cell1)
                    self.cells.matrix[self.cell1.pos] = self.cell1.mark
                    self.cells.positioning()
                    self.switch_turn()
                elif ((250<event.pos[0]<=500) and event.pos[1]<=250) and self.cells.matrix[1] == 'empty':
                    self.cell2 = game_board.GameBoardCell(1,'circle')
                    self.cells.add(self.cell2)
                    self.cells.matrix[self.cell2.pos] = self.cell2.mark
                    self.cells.positioning()
                    self.switch_turn()
                elif (event.pos[0]>500 and event.pos[1]<=250) and self.cells.matrix[2] == 'empty':
                    self.cell3 = game_board.GameBoardCell(2,'circle')
                    self.cells.add(self.cell3)
                    self.cells.matrix[self.cell3.pos] = self.cell3.mark
                    self.cells.positioning()
                    self.switch_turn()
                elif (event.pos[0]<=250 and (250<event.pos[1]<=500)) and self.cells.matrix[3] == 'empty':
                    self.cell4 = game_board.GameBoardCell(3,'circle')
                    self.cells.add(self.cell4)
                    self.cells.matrix[self.cell4.pos] = self.cell4.mark
                    self.cells.positioning()
                    self.switch_turn()
                elif ((250<event.pos[0]<=500) and (250<event.pos[1]<=500)) and self.cells.matrix[4] == 'empty':
                    self.cell5 = game_board.GameBoardCell(4,'circle')
                    self.cells.add(self.cell5)
                    self.cells.matrix[self.cell5.pos] = self.cell5.mark
                    self.cells.positioning()
                    self.switch_turn()
                elif (event.pos[0]>500 and (250<event.pos[1]<=500)) and self.cells.matrix[5] == 'empty':
                    self.cell6 = game_board.GameBoardCell(5,'circle')
                    self.cells.add(self.cell6)
                    self.cells.matrix[self.cell6.pos] = self.cell6.mark
                    self.cells.positioning()
                    self.switch_turn()
                elif (event.pos[0]<=250 and event.pos[1]>500) and self.cells.matrix[6] == 'empty':
                    self.cell7 = game_board.GameBoardCell(6,'circle')
                    self.cells.add(self.cell7)
                    self.cells.matrix[self.cell7.pos] = self.cell7.mark
                    self.cells.positioning()
                    self.switch_turn()
                elif ((250<event.pos[0]<=500) and event.pos[1]>500) and self.cells.matrix[7] == 'empty':
                    self.cell8 = game_board.GameBoardCell(7,'circle')
                    self.cells.add(self.cell8)
                    self.cells.matrix[self.cell8.pos] = self.cell8.mark
                    self.cells.positioning()
                    self.switch_turn()
                elif (event.pos[0]>500 and event.pos[1]>500) and self.cells.matrix[8] == 'empty':
                    self.cell9 = game_board.GameBoardCell(8,'circle')
                    self.cells.add(self.cell9)
                    self.cells.matrix[self.cell9.pos] = self.cell9.mark
                    self.cells.positioning()
                    self.switch_turn()
                else:
                    print('That cell is already taken, click again')
            else:
                if (event.pos[0]<=250 and event.pos[1]<=250) and self.cells.matrix[0] == 'empty':
                    self.cell1 = game_board.GameBoardCell(0,'cross')
                    self.cells.add(self.cell1)
                    self.cells.matrix[self.cell1.pos] = self.cell1.mark
                    self.cells.positioning()
                    self.switch_turn()
                elif ((250<event.pos[0]<=500) and event.pos[1]<=250) and self.cells.matrix[1] == 'empty':
                    self.cell2 = game_board.GameBoardCell(1,'cross')
                    self.cells.add(self.cell2)
                    self.cells.matrix[self.cell2.pos] = self.cell2.mark
                    self.cells.positioning()
                    self.switch_turn()
                elif (event.pos[0]>500 and event.pos[1]<=250) and self.cells.matrix[2] == 'empty':
                    self.cell3 = game_board.GameBoardCell(2,'cross')
                    self.cells.add(self.cell3)
                    self.cells.matrix[self.cell3.pos] = self.cell3.mark
                    self.cells.positioning()
                    self.switch_turn()
                elif (event.pos[0]<=250 and (250<event.pos[1]<=500)) and self.cells.matrix[3] == 'empty':
                    self.cell4 = game_board.GameBoardCell(3,'cross')
                    self.cells.add(self.cell4)
                    self.cells.matrix[self.cell4.pos] = self.cell4.mark
                    self.cells.positioning()
                    self.switch_turn()
                elif ((250<event.pos[0]<=500) and (250<event.pos[1]<=500)) and self.cells.matrix[4] == 'empty':
                    self.cell5 = game_board.GameBoardCell(4,'cross')
                    self.cells.add(self.cell5)
                    self.cells.matrix[self.cell5.pos] = self.cell5.mark
                    self.cells.positioning()
                    self.switch_turn()
                elif (event.pos[0]>500 and (250<event.pos[1]<=500)) and self.cells.matrix[5] == 'empty':
                    self.cell6 = game_board.GameBoardCell(5,'cross')
                    self.cells.add(self.cell6)
                    self.cells.matrix[self.cell6.pos] = self.cell6.mark
                    self.cells.positioning()
                    self.switch_turn()
                elif (event.pos[0]<=250 and event.pos[1]>500) and self.cells.matrix[6] == 'empty':
                    self.cell7 = game_board.GameBoardCell(6,'cross')
                    self.cells.add(self.cell7)
                    self.cells.matrix[self.cell7.pos] = self.cell7.mark
                    self.cells.positioning()
                    self.switch_turn()
                elif ((250<event.pos[0]<=500) and event.pos[1]>500) and self.cells.matrix[7] == 'empty':
                    self.cell8 = game_board.GameBoardCell(7,'cross')
                    self.cells.add(self.cell8)
                    self.cells.matrix[self.cell8.pos] = self.cell8.mark
                    self.cells.positioning()
                    self.switch_turn()
                elif (event.pos[0]>500 and event.pos[1]>500) and self.cells.matrix[8] == 'empty':
                    self.cell9 = game_board.GameBoardCell(8,'cross')
                    self.cells.add(self.cell9)
                    self.cells.matrix[self.cell9.pos] = self.cell9.mark
                    self.cells.positioning()
                    self.switch_turn()
    
    def loop(self):
        self.cells.update()
        self.final()
        if self.finish:
            if self.actual_time+2000<=pygame.time.get_ticks():
                return self.game.change_state('RESULT')
    
    def update(self,screen):
        self.paint(screen)
        self.cells.draw(screen)
        
        pygame.display.flip()

