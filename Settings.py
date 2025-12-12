import pygame
import random
from enum import Enum,auto


class GameState(Enum):
    MainMenu = auto()
    Play = auto()
    GameOver = auto()
#--------------------------------------------------------------------




#--------------------------------------------------------------------



w_Width,w_Height = 500, 500
global state
state = GameState.MainMenu
running = True
displaySurf = pygame.display.set_mode((w_Width,w_Height))
pygame.display.set_caption("SnakeClone")

