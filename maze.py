import pygame

WIDTH = 700
HEIGHT = 600
SIZE = (WIDTH,HEIGHT)
FPS = 60

win = pygame.display.set_mode((700,600))

backgoround = pygame.transform.scale(
                pygame.image.load("background.jpg"),
                SIZE
)

pygame.display.set_caption("Підвал порошенка.Автора не скажу бо він мене знайде")
clock = pygame.time.Clock()



pygame.mixer.init()
pygame.mixer_music.load("jungles.ogg")
pygame.mixer_music.play()

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, filename:str, size:tuple[int,int], coords:tuple[int,int], speed:int):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(filename),size)
        self.rect =self.image.get_rect(center=coords)
        self.speed = speed
    
    def reset(self, window:pygame.Surface):
        window.blit(self.image, self.rect)

class Player(GameSprite):
    def update(self):
        keys = pygame.key.get_pressed() 
        if keys[pygame.K_UP] and self.rect.y >=0:
            self.rect.y -= 5
        if keys[pygame.K_DOWN] and self.rect.y <= HEIGHT - self.rect.height:
            self.rect.y += 5
        if keys[pygame.K_RIGHT]and self.rect.x <= WIDTH - self.rect.width:
            self.rect.x += 5
        if keys[pygame.K_LEFT]and self.rect.x >= 0:
            self.rect.x -= 5

class Enemy(GameSprite):
    def update(self,x1,x2):
        self.rect.x += self.speed
        if self.rect.x >= x2 or self.rect.x <=x1:
            self.speed = -self.speed

class Wall:
    def __init__(self,coords:tuple[int,int], size:tuple[int,int], color:tuple[int,int,int]):
        self.rect = pygame.Rect(coords,size)
        self.color = color
    def draw(self,window:pygame.Surface,width=0):
        pygame.draw.rect(window, self.color, self.rect,width=width)
       


player = Player("hero.png",(70,60),(50,HEIGHT-150),5)
enemy = Enemy("cyborg.png",(60,50),(WIDTH-150,HEIGHT//2),5)
gold = GameSprite("treasure.png",(60,50),(WIDTH-100,HEIGHT-95),5)
gold_false = GameSprite("treasure.png",(60,50),(216,536),5)

wall_0 = Wall((0,0),(WIDTH,HEIGHT), (10,170,40))

wall = [
    Wall((10,60), (400,10), (10,170,80)),
    Wall((400,60), (10,400), (10,170,80)),
    Wall((270,150), (10,600), (10,170,80)),
    Wall((510,150), (10,600), (10,170,80)),
    ]

game = True
finish = False
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
    if not finish:
        win.blit(backgoround,(0,0))

        player.update()
        player.reset(win)

        enemy.update(WIDTH//2, WIDTH- 100)
        enemy.reset(win)

        gold.reset(win)
        gold_false.reset(win)
        if pygame.sprite.collide_rect(player,enemy):
            finish = True
            kick = pygame.mixer.Sound("kick.ogg")
            kick.play()
            pygame.font.init()
            font1 = pygame.font.Font(None,50)
            text = font1.render("POROCHENCO FIND YOU",True,(255,0,0))
            win.blit(text, (WIDTH//2, HEIGHT//2))
            

        if pygame.sprite.collide_rect(player,gold):
            finish = True
            kick = pygame.mixer.Sound("money.ogg")
            kick.play()
            pygame.font.init()
            font1 = pygame.font.Font(None,50)
            text = font1.render("POROCHENCO CAN'T FIND YOU",True,(0,250,0))
            win.blit(text, (100 , HEIGHT//2))


        wall_0.draw(win,width = 5)



        for w in wall:
            w.draw(win)
            if pygame.sprite.collide_rect(player,w):
                finish = True
                kick = pygame.mixer.Sound("kick.ogg")
                kick.play()


                pygame.font.init()
                font1 = pygame.font.Font(None,50)
                text = font1.render("POROCHENCO FIND YOU",True,(255,0,0))
                win.blit(text, (WIDTH//2 -200, HEIGHT//2))




    pygame.display.update()
    clock.tick(FPS)


































































































































