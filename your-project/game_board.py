#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pygame
from pgu import text

class GameBoardCell(pygame.sprite.Sprite):
    def __init__(self,pos,mark):
        super().__init__()
        self.image = pygame.image.load(mark+'.png')
        self.rect = self.image.get_rect()
        self.pos = pos
        self.mark = mark

#    def update(self):
#        if self.click:
#            self.empty = False

class GameBoard(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.matrix = ['empty', 'empty', 'empty','empty','empty','empty',
                       'empty','empty','empty']
        self.positions = ((125,125),(375,125),(625,125),(125,375),(375,375),(625,375),(125,625),(375,625),(625,625))
    
    def positioning(self):
        for cell in self:
            cell.rect.center = self.positions[cell.pos]

class Button(pygame.sprite.Sprite):
    def __init__(self,im,pos):
        super().__init__()
        self.image=pygame.image.load(im)
        self.rect=self.image.get_rect()
        self.rect.center=pos
        self.click = False

