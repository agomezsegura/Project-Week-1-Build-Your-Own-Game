#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pygame
from pgu import text

class GameBoardCell(pygame.sprite.Sprite):
    def __init__(self,pos,mark):
        super().__init__()
        self.image = pygame.image.load(mark+'.png')
        self.rect = self.image.get_rect()
        self.rect.center = pos[0]
        self.num = pos[1]
        self.mark = mark

#    def update(self):
#        if self.click:
#            self.empty = False

class GameBoard(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.matrix = ['empty', 'empty', 'empty','empty','empty','empty',
                       'empty','empty','empty']

