from Settings import *

class Follower(pygame.sprite.Sprite):
    def __init__(self, groups, spawn):
        super().__init__(groups)
        self.direction = pygame.math.Vector2(0,1)
        self.speed = 75
        self.rect = pygame.rect.FRect((spawn),(30,30))
        self.pos = pygame.math.Vector2(self.rect.center) 
    # def movement(self):
       
    #     if self.rect.right < 0:
    #         self.rect.left = w_Width
    #     if self.rect.left > w_Width:
    #         self.rect.right = 0

    #     if self.rect.bottom < 0:
    #         self.rect.top = w_Height
    #     if self.rect.top > w_Height:
    #         self.rect.bottom = 0

    def update(self, dt):
        pygame.draw.rect(displaySurf, 'white', self.rect,0, 8).inflate(5,5)