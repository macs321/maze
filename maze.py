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
        win.blit(self.image, self.rect)

player = GameSprite("hero.png",(70,60),(50,HEIGHT-150),5)
enemy = GameSprite("cyborg.png",(60,50),(WIDTH-150,HEIGHT//2),5)
gold = GameSprite("treasure.png",(60,50),(WIDTH-150,HEIGHT-150),5)


game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    win.blit(backgoround,(0,0))
    player.reset(win)
    enemy.reset(win)
    gold.reset(win)

    pygame.display.update()
    clock.tick(FPS)




































































