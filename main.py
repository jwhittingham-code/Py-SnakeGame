from Settings import *
import Player as P
import Follower as F

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
