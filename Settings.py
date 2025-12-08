import pygame
import random

def quitPython():
    running = False
    pygame.quit()

w_Width,w_Height = 500, 500
running = True
displaySurf = pygame.display.set_mode((w_Width,w_Height))
pygame.display.set_caption("SnakeClone")
