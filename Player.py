from Settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.pos = pygame.math.Vector2(500,500)
        self.rect = pygame.rect.FRect((self.pos),(50,50))
        
    def update(self, dsurf, dt):
        pygame.draw.rect(dsurf, 'red', self.rect)
        self.pos.x += 50 *dt
        self.rect.center = self.pos