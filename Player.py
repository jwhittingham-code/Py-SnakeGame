from Settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.direction = pygame.math.Vector2(0,1)
        self.points = 0
        self.speed = 15
        self.rect = pygame.rect.FRect((w_Width/2, w_Height/2),(30,30))
        self.pos = pygame.math.Vector2(self.rect.center) 
        self.timer = 0
        self.move = False

    def getInputs(self):
        self.keys = pygame.key.get_pressed()
        if self.keys[pygame.K_RIGHT] and self.direction.x != -1:
            self.direction.x = 1
            self.direction.y = 0
        elif self.keys[pygame.K_LEFT] and self.direction.x != 1:
            self.direction.x = -1
            self.direction.y = 0

        if self.keys[pygame.K_DOWN] and self.direction.y != -1:
            self.direction.x = 0
            self.direction.y = 1
        elif self.keys[pygame.K_UP] and self.direction.y != 1:
            self.direction.x = 0
            self.direction.y = -1

    def movement(self):
        currentTime = pygame.time.get_ticks() /50
        
        if self.move == False:
            self.pos = pygame.math.Vector2(self.rect.center)
            self.rect.center += self.direction * self.speed
            self.move = True
            self.timer = currentTime + 2
        if currentTime > self.timer:
            self.move = False
                
        if self.rect.right < 0:
            self.rect.left = w_Width
        if self.rect.left > w_Width:
            self.rect.right = 0

        if self.rect.bottom < 0:
            self.rect.top = w_Height
        if self.rect.top > w_Height:
            self.rect.bottom = 0

    def update(self, dt):
        pygame.draw.rect(displaySurf, 'white', self.rect,0,10)
        self.getInputs()
        self.movement()