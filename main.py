from Settings import *
import Player as P
import Follower as  F
import GameLoop


#Classes
#--------------------------------------------------------------------------------
  
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
            appleSound.play()
            Apple(allsprites)
            x = len(followers) -1
            for i in range(2):
                followers.append(F.Follower(allsprites,followers[x].pos))

#Setup
#----------------------------------------------------------------------------------
pygame.init()

appleSound = pygame.mixer.Sound('Apple.wav')

clock = pygame.time.Clock()
running = True

allsprites = pygame.sprite.Group()
player = P.Player(allsprites)
Apple(allsprites)

font =pygame.font.Font(None, 250)
followers = [player,F.Follower(allsprites , (player.rect.centerx, player.rect.centery )),F.Follower(allsprites, (player.rect.centerx,player.rect.centery ))]
points = []

#Game loop
#-----------------------------------------------------------------------------------
while running:
    dt = clock.tick() / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    displaySurf.fill('black')

    GameLoop.gameloop(player,followers)
    #update display
    GameLoop.displayScore(player,font)
    allsprites.update(dt)
    pygame.display.update()
    if player.colour == 'red':
        running = False

pygame.quit()