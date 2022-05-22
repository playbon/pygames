
from tracemalloc import stop
from pygame import*
mixer.init()
mixer.music.load("битва.mp3")
mixer.music.play()
kick = mixer.Sound("победа.mp3")
kick2 = mixer.Sound("поражение.mp3")
class gameSprite(sprite.Sprite):
    def __init__(self, picture, width, height, x,y,speed, x1 ,x2):
        super().__init__()
        self.image=transform.scale(image.load(picture),(width, height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x1=x1
        self.x2=x2
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(gameSprite):
    def update(self):
        self.keys = key.get_pressed()
        if self.keys[K_w] and self.rect.y > 5 :
            self.rect.y -= self.speed
        if self.keys[K_s] and self.rect.y < 480 :
            self.rect.y += self.speed
        if self.keys[K_a] and self.rect.x > 5 :
            self.rect.x -= self.speed
        if self.keys[K_d] and self.rect.x < 600 :
            self.rect.x += self.speed
class Enemy(gameSprite):
    dir = "left"
    def update(self):
        if self.dir == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
        if self.rect.x <= self.x1:
            self.dir = "right"
        if self.rect.x >= self.x2:
            self.dir = "left"
class Wall(sprite.Sprite):
    def __init__ (self,color_1, color_2, color_3,wall_x,wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1 
        self.color_2 = color_2
        self.color_3 = color_3
        self.wall_width = wall_width
        self.wall_height = wall_height
        self.image = Surface((self.wall_width,self.wall_height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
window = display.set_mode((700, 500))
display.set_caption("WW3")
background = transform.scale(image.load("фон.jpg"),(700, 500))
window.blit(background, (0,0))
clock = time.Clock()
FPS = 60
GREEN = (0,255,0)
win_width = 700
win_height = 500
player1 = Player("сталин.png", 75,55,100,5,10,0,0)
player2 = Enemy("гитлер.png", 75,55,40,100,1,5,600)
player4 = Enemy("гитлер.png",75 ,55,400,200,1,5,600)
player3 = gameSprite("путин.png", 200,110,220,300,0,0,0)
game = True
wall1 = Wall(70,45,120,0,2,35,500)
wall2 = Wall(70,45,120,100,250,700,20)
wall3 = Wall(70,45,120,30,60,500,20)
wall4 = Wall(70,45,120,675,2,35,500)
finish = False
while game:
    if not finish:
        window.blit(background, (0,0))
        player2.reset()
        player2.update()
        player1.reset()
        player1.update()
        player3.reset()
        player4.reset()
        player4.update()
        wall1.draw_wall()
        wall2.draw_wall()
        wall3.draw_wall()
        wall4.draw_wall()
    if sprite.collide_rect(player1,player3):
        finish = True
        win = transform.scale(image.load("победа.jfif"),(700, 500))
        window.blit(win, (0,0))
        mixer.music.stop()
        kick.play()
    if sprite.collide_rect(player1,player2) or sprite.collide_rect(player1,player4) or sprite.collide_rect(player1,wall1) or sprite.collide_rect(player1,wall2) or sprite.collide_rect(player1,wall3) or sprite.collide_rect(player1,wall4):
        finish = True
        win = transform.scale(image.load("поражение.JPG"),(700, 500))
        window.blit(win, (0,0))
        mixer.music.stop()
        kick2.play()

    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(FPS)
    
