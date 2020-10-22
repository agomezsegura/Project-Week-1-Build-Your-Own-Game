#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pygame;
from pygame.locals import *
from pgu import engine
import game_board
import play_vsCPU
import play_pvp


# In[2]:


class Tic_Tac_Toe(engine.Game):
    def __init__(self):
        super().__init__()
        pygame.mixer.pre_init(44100, -16, 2, 512)
        pygame.init()
        self.myFont = pygame.font.Font('Raind___.TTF',80)
        self.screen = pygame.display.set_mode((750,750), SWSURFACE)
        self.crono = pygame.time.Clock()
        self._init_state_machine()
        self.result = ''
        
    def _init_state_machine(self):
        self.menu_state = Menu(self)
        self.playervsCPU_state = play_vsCPU.PlayerVSCPU(self)
        self.playervsplayer_state = play_pvp.PlayerVSPlayer(self)
        self.result_state = Result(self)
        self.quit_state = engine.Quit(self)
    
    def change_state(self, transition=None):
        """
        Implements the state machine of the game.
        Given self.state and an optional parameter indicating 
        the kind of transition, computes and returns the new state
        """
        if self.state is self.menu_state:
            if transition == 'EXIT':
                new_state = self.quit_state
            elif transition == 'PLAYERVSCPU':
                new_state = self.playervsCPU_state
            elif transition == 'PLAYERVSPLAYER':
                new_state = self.playervsplayer_state
            else:
                raise ValueError('Unknown transition indicator')
        elif self.state is self.playervsCPU_state:
            if transition == 'EXIT':
                new_state = self.quit_state
            elif transition == 'RESULT':
                new_state = self.result_state
            else:
                raise ValueError('Unknown transition indicator')
        elif self.state is self.playervsplayer_state:
            if transition == 'EXIT':
                new_state = self.quit_state
            elif transition == 'RESULT':
                new_state = self.result_state
            else:
                raise ValueError('Unknown transition indicator')
        elif self.state is self.result_state:
            if transition == 'EXIT':
                new_state = self.quit_state
            elif transition == 'RETRY':
                if self.result == 'Player wins' or self.result == 'CPU wins' or self.result == 'DrawPvsCPU':
                    new_state = self.playervsCPU_state
                    new_state.init()
                else:
                    new_state = self.playervsplayer_state
                    new_state.init()
            elif transition == 'MENU':
                new_state = self.menu_state
            else:
                raise ValueError('Unknown transition indicator')
        else:
            raise ValueError('Unknown game state value')
        return new_state
        
    def run(self):
        # Calls the main loop with the initial state
        # (self.menu, in this case)
        super().run(self.menu_state, self.screen)

##------------------------------------------------------Menu screen-------------------------------------------

class Menu(engine.State):
    def init(self):
        #self.image = pygame.image.load("env/menu_def.jpg") 
        #pygame.mixer.music.load("env/intro.ogg")
        #pygame.mixer.music.play()
        self.menuText = self.game.myFont.render('Tic-Tac-Toe',0,(255,255,255))
        self.pvCPU_button = game_board.Button("button_pvscpu.png",(250,500))
        self.pvp_button = game_board.Button("button_pvp.png",(500,500))
        self.buttons = pygame.sprite.Group()
        self.buttons.add(self.pvCPU_button)
        self.buttons.add(self.pvp_button)
        
    def paint(self, s):
        s.fill((0, 0, 0))
        s.blit(self.menuText,(70,170))
        #rect = self.image.get_rect()
        #rect.center = s.get_rect().center
        #s.blit(self.image, rect)

    def event(self,e): 
        if e.type is KEYDOWN:
            if e.key == K_ESCAPE:
                return self.game.change_state('EXIT')
        elif e.type is pygame.MOUSEBUTTONDOWN:
            for b in list(self.buttons):
                    if b.rect.collidepoint(e.pos):
                        if  b == self.pvCPU_button:
                            return self.game.change_state('PLAYERVSCPU')
                        else:
                            return self.game.change_state('PLAYERVSPLAYER')
    def loop(self):
        pass
    
    def update(self,screen):
        self.paint(screen)
        self.buttons.draw(screen)
        
        pygame.display.flip()

##------------------------------------------------------Result screen ---------------------------------

class Result(engine.State):
    def init(self):
        #self.image = pygame.image.load("env/menu_def.jpg") 
        #pygame.mixer.music.load("env/intro.ogg")
        #pygame.mixer.music.play()
        self.retry_button = game_board.Button("button_pvscpu.png",(250,500))
        self.menu_button = game_board.Button("button_pvp.png",(500,500))
        self.buttons = pygame.sprite.Group()
        self.buttons.add(self.retry_button)
        self.buttons.add(self.menu_button)
        
    def paint(self, s):
        s.fill((0, 0, 0))
        #rect = self.image.get_rect()
        #rect.center = s.get_rect().center
        #s.blit(self.image, rect)

    def event(self,e): 
        if e.type is KEYDOWN:
            if e.key == K_ESCAPE:
                return self.game.change_state('EXIT')
        elif e.type is pygame.MOUSEBUTTONDOWN:
            for b in list(self.buttons):
                    if b.rect.collidepoint(e.pos):
                        if  b == self.retry_button:
                            return self.game.change_state('RETRY')
                        elif b == self.menu_button:
                            return self.game.change_state('MENU')
    def loop(self):
        pass
    
    def update(self,screen):
        self.paint(screen)
        self.buttons.draw(screen)
        
        pygame.display.flip()
def main():
    game = Tic_Tac_Toe()
    game.run()


if __name__ == "__main__":
    main()

