from string import whitespace
from pygame import* 
import random
from random import choice

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):

    def update_first(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - self.rect.height:
            self.rect.y += self.speed

    def update_second(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - self.rect.height:
            self.rect.y += self.speed

class Ball(GameSprite):
    def update(self):
        global score1, score2
        if self.rect.y < 0 or self.rect.y > win_height - self.rect.height:
            self.y_speed *= -1
        if sprite.collide_rect(player1, self) or sprite.collide_rect(self, player2):
            self.x_speed *= -1
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
        if self.rect.x > win_width - self.rect.width:
            score1 += 1
            self.rect.centerx = win_width / 2
            self.rect.centery = win_height / 2
            self.x_speed, self.y_speed = random.choice(speeds)
            self.x_speed *= random.choice([-1, 1])
            self.y_speed *= random.choice([-1, 1])
        if self.rect.x < 0:
            score2 += 1
            self.rect.centerx = win_width / 2
            self.rect.centery = win_height / 2
            self.x_speed, self.y_speed = random.choice(speeds)
            self.x_speed *= random.choice([-1, 1])
            self.y_speed *= random.choice([-1, 1])


win_height = 700
win_width = 1250
display.set_caption('Ping - Pong')
window = display.set_mode((win_width, win_height))
back = transform.scale(image.load('bbor.png'),(win_width, win_height))

player1 = Player('eed.png', 30, 300, 30, 200, 6)
score1 = 0
player2 = Player('eed.png', 1190, 300, 30, 200, 6 )
score2 = 0
ball = Ball('bbor.png', (win_width/2), (win_height/2), 30, 50, 5)

speeds = [(3, 5), (2, 3), (3, 4)]
ball.x_speed, ball.y_speed = random.choice(speeds)




font.init()
FONT = font.SysFont('comics sans ms', 20, bold = True)

run = True
game = True
clock = time.Clock()
FPS = 60
#

while game == True:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.fill((100, 100, 100))       
    if run:
        player1.update_first()
        player2.update_second()
        player1.reset()
        player2.reset()
        ball.reset()
        ball.update()
        score = FONT.render(str(score1) + "  " + str(score2), True, (0, 0, 0))
        fps = int(clock.get_fps())
        fps_text = FONT.render(f"FPS: {fps}", True, (255, 255, 255))
        window.blit(score, ((win_width/2), (200)))
        window.blit(fps_text, (320, 120))
    display.update()    
    clock.tick(FPS)