from Settings import *
import Player as P
import Follower as  F
import GameLoop
import Menu
import json

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

def quitPython():
    jfile["score"] = highscore
    with open("HighScore.json","w") as file:
        json.dump(jfile, file)
    pygame.quit()
#----------------------------------------------------------------------------------
pygame.init()

appleSound = pygame.mixer.Sound('Apple.wav')
selectSound = pygame.mixer.Sound('MenuSelect.wav')

clock = pygame.time.Clock()


allsprites = pygame.sprite.Group()
player = P.Player(allsprites)
Apple(allsprites)

font =pygame.font.Font(None, 250)
test =font.render("test",True,"white")

menuFont = pygame.font.Font(None, 30)
menuTitleFont = pygame.font.Font(None, 100)
followers = [player,F.Follower(allsprites , (player.rect.centerx, player.rect.centery )),F.Follower(allsprites, (player.rect.centerx,player.rect.centery ))]
jfile = {}
try:
    with open("HighScore.json","r") as file:
        jfile = json.load(file)
    highscore = jfile["score"]
except:
    highscore = 0 

#Game loop
#-----------------------------------------------------------------------------------
while running:
    dt = clock.tick() / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitPython

    displaySurf.fill('black')
    
    match state:
        case GameState.MainMenu:
           state = Menu.menu(menuTitleFont,menuFont,appleSound,selectSound,highscore)
        
        case GameState.Play:

            GameLoop.gameloop(player,followers)
            GameLoop.displayScore(player,font)
            allsprites.update(dt)
            
            if player.collide == True:
                state = GameState.MainMenu
                if player.points > highscore:
                    highscore = player.points
                for i in followers:
                        i.kill()
                player = P.Player(allsprites)        
                followers = [player,F.Follower(allsprites , (player.rect.centerx, player.rect.centery )),F.Follower(allsprites, (player.rect.centerx,player.rect.centery ))]
               



            key = pygame.key.get_just_pressed()
            if key[pygame.K_ESCAPE]:
                state = GameState.MainMenu

           
        
        case GameState.GameOver:
            quitPython()
        case _:
            quitPython()
    
    pygame.display.update()
    print(highscore)
    
quitPython()