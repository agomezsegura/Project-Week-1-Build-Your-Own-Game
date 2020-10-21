#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pygame
from pgu import text

class GameBoardCell(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("circle.png")
        self.cross = pygame.image.load("cross.png")
        self.rect = self.image.get_rect()
        self.click = False
        self.empty = True

    def update(self):
        if self.click:
            self.empty = False

class GameBoard(pygame.sprite.Group):
    def __init__(self,pos1,pos2,pos3,pos4,pos5,pos6,pos7,pos8,pos9):
        super().__init__()
        self.pos1=pos1
        self.pos2=pos2
        self.pos3=pos3
        self.pos4=pos4
        self.pos5=pos5
        self.pos6=pos6
        self.pos7=pos7
        self.pos8=pos8
        self.pos9=pos9
    
    def positioning(self):
        if len(self.sprites())==0:
            pass
        elif len(self.sprites())==1:
            self.sprites()[0].rect.topleft=self.pos1
        elif len(self.sprites())==2:
            self.sprites()[0].rect.topleft=self.pos1
            self.sprites()[1].rect.topleft=self.pos2
        elif len(self.sprites())==3:
            self.sprites()[0].rect.topleft=self.pos1
            self.sprites()[1].rect.topleft=self.pos2
            self.sprites()[2].rect.topleft=self.pos3
        elif len(self.sprites())==4:
            self.sprites()[0].rect.topleft=self.pos1
            self.sprites()[1].rect.topleft=self.pos2
            self.sprites()[2].rect.topleft=self.pos3
            self.sprites()[3].rect.topleft=self.pos4
        elif len(self.sprites())==5:
            self.sprites()[0].rect.topleft=self.pos1
            self.sprites()[1].rect.topleft=self.pos2
            self.sprites()[2].rect.topleft=self.pos3
            self.sprites()[3].rect.topleft=self.pos4
            self.sprites()[4].rect.topleft=self.pos5
        elif len(self.sprites())==6:
            self.sprites()[0].rect.topleft=self.pos1
            self.sprites()[1].rect.topleft=self.pos2
            self.sprites()[2].rect.topleft=self.pos3
            self.sprites()[3].rect.topleft=self.pos4
            self.sprites()[4].rect.topleft=self.pos5
            self.sprites()[5].rect.topleft=self.pos6
        elif len(self.sprites())==7:
            self.sprites()[0].rect.topleft=self.pos1
            self.sprites()[1].rect.topleft=self.pos2
            self.sprites()[2].rect.topleft=self.pos3
            self.sprites()[3].rect.topleft=self.pos4
            self.sprites()[4].rect.topleft=self.pos5
            self.sprites()[5].rect.topleft=self.pos6
            self.sprites()[6].rect.topleft=self.pos7
        elif len(self.sprites())==8:
            self.sprites()[0].rect.topleft=self.pos1
            self.sprites()[1].rect.topleft=self.pos2
            self.sprites()[2].rect.topleft=self.pos3
            self.sprites()[3].rect.topleft=self.pos4
            self.sprites()[4].rect.topleft=self.pos5
            self.sprites()[5].rect.topleft=self.pos6
            self.sprites()[6].rect.topleft=self.pos7
            self.sprites()[7].rect.topleft=self.pos8
        elif len(self.sprites())==9:
            self.sprites()[0].rect.topleft=self.pos1
            self.sprites()[1].rect.topleft=self.pos2
            self.sprites()[2].rect.topleft=self.pos3
            self.sprites()[3].rect.topleft=self.pos4
            self.sprites()[4].rect.topleft=self.pos5
            self.sprites()[5].rect.topleft=self.pos6
            self.sprites()[6].rect.topleft=self.pos7
            self.sprites()[7].rect.topleft=self.pos8
            self.sprites()[8].rect.topleft=self.pos9

