from Settings import *
#import Player

#Classes
#--------------------------------------------------------------------------------

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
        

class Follower(pygame.sprite.Sprite):
    def __init__(self, groups, spawn):
        super().__init__(groups)
        self.direction = pygame.math.Vector2(0,1)
        self.speed = 75
        self.rect = pygame.rect.FRect((spawn),(30,30))
        self.pos = pygame.math.Vector2(self.rect.center) 
    def movement(self):
       
        if self.rect.right < 0:
            self.rect.left = w_Width
        if self.rect.left > w_Width:
            self.rect.right = 0

        if self.rect.bottom < 0:
            self.rect.top = w_Height
        if self.rect.top > w_Height:
            self.rect.bottom = 0

    def update(self, dt):
        pygame.draw.rect(displaySurf, 'white', self.rect,0, 8).inflate(5,5)

  
class Apple(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.pos = pygame.math.Vector2(random.randint(0,w_Width),random.randint(0,w_Height))     
        self.rect = pygame.rect.FRect(random.randint(0,w_Width),random.randint(0,w_Height), 10,10)

    def update(self, dt):
        pygame.draw.rect(displaySurf, 'green', self.rect)
        if self.rect.colliderect(player.rect):
            player.points += 1
            self.kill()
            Apple(allsprites)
            x = len(followers) -1
            for i in range(2):
                followers.append(Follower(allsprites,followers[x].pos))

#Functions
# ---------------------------------------------------------------------------------        
def displayScore():
    score = player.points
    textSurf = font.render(str(score),True, (30,30,30))
    textrect = textSurf.get_frect(center = (w_Width/2 , w_Height/2))
    displaySurf.blit(textSurf,textrect)

#Setup
#----------------------------------------------------------------------------------
pygame.init()
pygame.display.set_caption("SnakeClone")

clock = pygame.time.Clock()
running = True
displaySurf = pygame.display.set_mode((w_Width,w_Height))
allsprites = pygame.sprite.Group()
player = Player(allsprites)
Apple(allsprites)

font =pygame.font.Font(None, 250)
followers = [player,Follower(allsprites , (player.rect.centerx, player.rect.centery )),Follower(allsprites, (player.rect.centerx,player.rect.centery ))]
points = []

#Game loop
#-----------------------------------------------------------------------------------
while running:
    dt = clock.tick() / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    displaySurf.fill('black')

    #updating and moving "followers"
    for x in range(len(followers)):
        y = x - 1
        s = 0.015
        
        if player.pos != pygame.math.Vector2(player.rect.center):
            if x > 0: 
                if followers[x] != player and player.move == False:
                    followers[x].rect.center = followers[y].pos
                if player.move ==True:
                    followers[x].pos = followers[x].rect.center
                if x > 2:
                    if followers[x].rect.colliderect(player.rect):
                        running = False
           
    #update display
    displayScore()
    allsprites.update(dt)
    pygame.display.update()

pygame.quit()
